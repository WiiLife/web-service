#!/bin/bash

echo "Waiting for MongoDB to be ready..."

# Wait until MongoDB is available
until pipenv run python -c "
from pymongo import MongoClient
import sys
try:
    MongoClient('mongodb://ml_user:securepassword@mongodb:27017/moores_law_db?authSource=moores_law_db').admin.command('ping')
except Exception:
    sys.exit(1)
"; do
  echo "MongoDB not available - retrying..."
  sleep 2
done

echo "MongoDB is available, inserting data..."
pipenv run python download_data.py
pipenv run python add_data_to_mongodb.py

echo "Starting Flask web server..."
pipenv run python web_service_project/run_web_service.py
