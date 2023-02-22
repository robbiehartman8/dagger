# az login

# az ad sp create-for-rbac --name gprc-servers
# docker network create dagger

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

cd /Users/roberthartman/Desktop/repos/dagger
docker build -t server_read_identity:latest -f services/identity/read/Dockerfile .
docker build -t server_create_update_identity -f services/identity/create_update/Dockerfile .
docker build -t server_appear_user_id_identity -f services/identity/appear_user_id/Dockerfile .

docker run -d -p 50052:50052 --net dagger --name server_read_identity server_read_identity
docker run -d -p 50051:50051 --net dagger --name server_create_update_identity server_create_update_identity
docker run -d -p 50054:50054 --net dagger --name server_appear_user_id_identity server_appear_user_id_identity

docker image prune --force

# {
#   "appId": "811a978e-8e50-4570-ade7-d991fd0f1128",
#   "displayName": "gprc-servers",
#   "password": "jF08Q~5aFHJTaInT8aWjhULkIrSzUHhri.hYvbeU",
#   "tenant": "4a5aa09d-9d1d-4f04-a983-271892a66895"
# }

