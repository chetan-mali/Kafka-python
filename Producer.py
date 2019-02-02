from confluent_kafka import Producer
 
p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce('topic', key='message', value="Hello")
p.flush(30)
