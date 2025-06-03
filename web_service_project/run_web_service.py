from flask import Flask
from pymongo import MongoClient
from web_service_project.routes.cpu_web_service import cpu_bp
from web_service_project.routes.gpu_web_service import gpu_bp
from web_service_project.routes.ram_web_service import ram_bp


def create_app():
    app = Flask(__name__)

    client = MongoClient("mongodb://ml_user:securepassword@mongodb:27017/moores_law_db?authSource=moores_law_db")
    # client = MongoClient("mongodb://localhost:27017/")
    db = client["moores_law_db"]

    # Register Blueprints
    app.register_blueprint(cpu_bp, url_prefix="/cpu")
    app.register_blueprint(gpu_bp, url_prefix="/gpu")
    app.register_blueprint(ram_bp, url_prefix="/ram")

    @app.route("/")
    def home():
        return {"message": "welcome to our web service",
                "authors": ["William Ambrosetti", "Youssef Sedra"],
                "methods": ["get_component_names",
                            "get_components_features",
                            "get_all_collections",
                            "get_a_collection",
                            "check_if_component_exists",
                            "get_specific_component_s",
                            "add_data",
                            "add_many",
                            "update_a_component",
                            "delete_component_s",
                            "delete_collection",
                            "plot_components"]}, 200

    @app.route("/all_components")
    def get_all_comp():
        collections = db.list_collection_names()
        all_comp = []

        for col in collections:
            all_comp.append(list(db[col].find({}, {"_id": 0})))

        # flattened list
        return [item for sublist in all_comp for item in sublist]

    @app.route("/component_names")
    def get_component_names():
        return db.list_collection_names()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5050)
