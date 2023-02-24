
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

cd /Users/roberthartman/Desktop/repos/dagger
docker build -t server_read_identity:latest -f services/identity/read/Dockerfile .
docker build -t server_create_update_identity -f services/identity/create_update/Dockerfile .
docker build -t server_appear_user_id_identity -f services/identity/appear_user_id/Dockerfile .

cd /Users/roberthartman/Desktop/repos/dagger/docker

docker-compose up -d

sleep 30

docker-compose exec kafka1 kafka-topics --create --bootstrap-server kafka1:9092 --replication-factor 1 --partitions 1 --topic provisioning
docker-compose exec kafka1 kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic deprovisioning
docker-compose exec kafka1 kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic attributeupdate

docker image prune --force
