from flask import Blueprint, request
from pymongo import MongoClient
from web_service_project.common_route_methods.parse import parse_query_string

cpu_bp = Blueprint('cpu', __name__)

client = MongoClient("mongodb://ml_user:securepassword@mongodb:27017/moores_law_db?authSource=moores_law_db")
# client = MongoClient("mongodb://localhost:27017/")
db = client["moores_law_db"]

collection = db["cpu"]


@cpu_bp.route("/", methods=["GET"])
def get_specific_data():

    query = request.args.to_dict()
    if not query:
        data = list(collection.find({}, {"_id": 0}))
        return data, 200

    mongo_query = parse_query_string(query)
    data = list(collection.find(mongo_query, {"_id": 0}))
    if data:
        return data, 200
    else:
        return data, 404


@cpu_bp.route("/", methods=["POST"])
def add_data():

    collection_feat = list(collection.find_one({}, {"_id": 0}).keys())

    data = request.get_json()
    if not data:
        return {"error": "No data provided"}, 400

    if collection_feat:

        if set(list(data.keys())) != set(collection_feat):
            return {"error": "data not in correct format",
                    "expected_keys": list(collection_feat),
                    "received_keys": list(data.keys())}, 400

        if collection.find_one(data):
            return {"error": "data already present"}, 409

        collection.insert_one(data)
        return {"message": "data inserted successfully"}, 201

    # collection is empty
    else:
        collection.insert_one(data)
        return {"message": "data inserted successfully"}, 201


@cpu_bp.route("/", methods=["PUT"])
def update_specific_component():

    data = request.get_json()
    query = parse_query_string(request.args.to_dict())

    if not data:
        return {"error": "No data provided"}, 400

    if not query:
        return {"error": "no query provided"}, 400

    try:
        match_count = collection.count_documents(query)

        if match_count == 0:
            return {"error": "Component not found"}, 404

        if match_count > 1:
            return {"error": "more than one component found"}, 404

    except Exception as e:
        return {"error": f"not able to update component: {e}"}, 500

    try:
        collection.update_one(query, {"$set": data})
        return {"message": "updated one component"}, 201

    except Exception as e:
        return {"error": f"not able to update component: {e}"}, 500


@cpu_bp.route("/", methods=["DELETE"])
def delete_component():

    component_type = collection.name
    query = parse_query_string(request.args.to_dict())

    if not query:   # deleting whole component if there is no query

        data = list(collection.find({}, {"_id": 0}))

        if not data:
            return {"message": f"nothing to remove in collection {component_type}"}, 200

        try:
            db.drop_collection(component_type)
            return {"message": f"removed collection {component_type}"}, 200

        except Exception as e:
            return {"error": f"not able to update component: {e}"}, 500

    try:
        match_count = collection.count_documents(query)

        if match_count == 0:
            return {"error": "Component(s) not found"}, 404

    except Exception as e:
        return {"error": f"not able to update component: {e}"}, 500

    try:
        collection.delete_many(query)
        return {"message": f"removed {match_count} component(s)"}, 201

    except Exception as e:
        return {"error": f"not able to update component: {e}"}, 500


