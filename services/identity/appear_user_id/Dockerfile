# Base image Python v3.9.12
FROM python:3.9.12

# AZ cli
RUN apt-get update
RUN apt-get install azure-cli -y

RUN az login --service-principal -u "811a978e-8e50-4570-ade7-d991fd0f1128" -p "jF08Q~5aFHJTaInT8aWjhULkIrSzUHhri.hYvbeU" --tenant "4a5aa09d-9d1d-4f04-a983-271892a66895"

# Copy requirements document file into image
COPY ./services/requirements.txt /app/requirements.txt

# Switch working directory
WORKDIR /app

# Upgrade PIP and install dependency packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy Python files to image
# Proto file
COPY ./services/identity/identity.proto /app/identity.proto
# Main python file
COPY ./services/identity/appear_user_id/server_appear_user_id.py /app/server_appear_user_id.py
# Identity files
COPY ./services/identity/identity_constants.py /app/identity_constants.py
COPY ./services/identity/identity_utilities.py /app/identity_utilities.py
# Utilities
COPY ./services/utilities/call_service_utilities.py /app/call_service_utilities.py
COPY ./services/utilities/config_utilities.py /app/config_utilities.py
COPY ./services/utilities/query_utilities.py /app/query_utilities.py
COPY ./services/utilities/service_utilities.py /app/service_utilities.py
COPY ./services/utilities/snowflake_connection_utilities.py /app/snowflake_connection_utilities.py
COPY ./services/utilities/redis_utilities.py /app/redis_utilities.py

# Create grpc files
RUN python -m grpc_tools.protoc --proto_path=. ./identity.proto --python_out=. --grpc_python_out=.

# Configure the container to run in an executed manner
ENTRYPOINT ["python"]

# Start Flask service
CMD ["server_appear_user_id.py"]