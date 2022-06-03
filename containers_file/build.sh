# Subindo os containers
sudo docker-compose -f kafka_docker_compose.yml -d 

# Acessando o Kafka
sudo docker exec -it kafka /bin/sh

# Criando os Primeiros Tópicos
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic books
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic magazines

# Listando todos os tópicos
# kafka-topics.sh --list --zookeeper zookeeper:2181

# Detalhando um tópico - Describe
kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic books

# Deletando um tópico
kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic books

# Acessando o Producer do Tópico
# Inserindo entradas no producer, exemplo = {'id':1,'name':'product', 'description':' a new product are available'}
kafka-console-producer.sh --broker-list kafka:9092 --topic books

# Acessando o Consumer do tópico
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic books

# Lendo todas as mensagem com o Consumer desde o inicio do Producer
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic books --from-beginner

