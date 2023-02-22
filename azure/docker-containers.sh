
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

cd /Users/roberthartman/Desktop/repos/dagger
docker build -t server_read_identity:latest -f services/identity/read/Dockerfile .
docker build -t server_create_update_identity -f services/identity/create_update/Dockerfile .
docker build -t server_appear_user_id_identity -f services/identity/appear_user_id/Dockerfile .

docker run -d -p 50052:50052 --net dagger --name server_read_identity server_read_identity
docker run -d -p 50051:50051 --net dagger --name server_create_update_identity server_create_update_identity
docker run -d -p 50054:50054 --net dagger --name server_appear_user_id_identity server_appear_user_id_identity

docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest

docker image prune --force


