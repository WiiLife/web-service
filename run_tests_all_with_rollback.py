import subprocess
from pymongo import MongoClient

DB_NAME = "moores_law_db"
MONGO_URI = "mongodb://ml_user:securepassword@localhost:27017/moores_law_db?authSource=moores_law_db"


def reset_database():
    print("Resetting database...")
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    for name in db.list_collection_names():
        db.drop_collection(name)
    print("Dropped all collections")

    # Run the add_data_to_mongodb.py inside Docker
    result = subprocess.run([
    "docker", "exec", "project-web_service-1", "pipenv", "run", "python", "/app/add_data_to_mongodb.py"
], capture_output=True, text=True)

    if result.returncode != 0:
        print("Error running add_data_to_mongodb.py inside container:")
        print(result.stderr)
    else:
        print("Reloaded data in MongoDB container")


def run_tests():
    test_files = [
        "./testing/test_cpu.py",
        "./testing/test_gpu.py",
        "./testing/test_main.py",
        "./testing/test_ram.py",
        "./testing/test_turn_dict_to_obj.py",
    ]

    for test_file in test_files:
        print(f"\nRunning {test_file}...")
        result = subprocess.run(["pytest", "-q", test_file], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Tests passed: {test_file}")
        else:
            print(f"Tests failed: {test_file}")
        reset_database()


if __name__ == "__main__":
    run_tests()
