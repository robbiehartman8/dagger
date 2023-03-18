
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

cd /Users/roberthartman/Desktop/repos/dagger
# identity
docker build -t server_read_identity:latest -f services/identity/read/Dockerfile .
docker build -t server_create_update_identity:latest -f services/identity/create_update/Dockerfile .
docker build -t server_appear_user_id_identity:latest -f services/identity/appear_user_id/Dockerfile .
docker build -t server_delete_identity:latest -f services/identity/delete/Dockerfile .
# brithright
docker build -t server_get_access_birthright:latest -f services/birthright/get_access/Dockerfile .

cd /Users/roberthartman/Desktop/repos/dagger/docker
docker-compose up -d

sleep 10

docker-compose exec kafka1 kafka-topics --create --bootstrap-server kafka1:9092 --replication-factor 1 --partitions 4 --topic identity_create
docker-compose exec kafka1 kafka-topics --create --bootstrap-server kafka1:9092 --replication-factor 1 --partitions 4 --topic identity_update
docker-compose exec kafka1 kafka-topics --create --bootstrap-server kafka1:9092 --replication-factor 1 --partitions 4 --topic identity_delete
docker-compose exec kafka1 kafka-topics --create --bootstrap-server kafka1:9092 --replication-factor 1 --partitions 4 --topic provisioning
docker-compose exec kafka1 kafka-topics --create --bootstrap-server kafka1:9092 --replication-factor 1 --partitions 4 --topic deprovisioning

docker image prune --force
