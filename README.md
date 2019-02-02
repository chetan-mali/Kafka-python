# Kafka using Python

Download Kafka from apache.claz.org/kafka/0.10.2.2/kafka_2.12-0.10.2.2.tgz

Start Kafka  server 
* sudo kafka_2.12-0.10.2.2/bin/kafka-server-start.sh kafka_2.12-0.10.2.2/config/server.properties

Create Topic 
* sudo kafka_2.12-0.10.2.2/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1  --partitions 1 --topic topicname

Consumer 
* sudo kafka_2.12-0.10.2.2/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic testing --from-beginning

Producer 
* sudo kafka_2.12-0.10.2.2/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testing
