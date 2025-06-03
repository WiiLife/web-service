FROM python:3.12

WORKDIR /app

# Install pipenv
RUN pip install pipenv

# -------------------------------------
# Step 1: Installing the pipfile and running the data setup
# -------------------------------------
# Add and install init requirements
COPY initialize/Pipfile init.Pipfile
COPY initialize/Pipfile.lock init.Pipfile.lock
RUN mv init.Pipfile Pipfile && mv init.Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile

# -------------------------------------
# Step 2: Installing and running webservice
# -------------------------------------
COPY web_service_project/Pipfile web.Pipfile
COPY web_service_project/Pipfile.lock web.Pipfile.lock
RUN rm Pipfile Pipfile.lock && mv web.Pipfile Pipfile && mv web.Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile

COPY web_service_project ./web_service_project
RUN pipenv run pip install -e ./web_service_project

COPY initialize/add_data_to_mongodb.py add_data_to_mongodb.py
COPY initialize/download_data.py download_data.py

ENV PYTHONPATH="/app"
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]