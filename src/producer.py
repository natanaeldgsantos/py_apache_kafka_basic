import time
import json
import random
from   datetime import datetime 
from   data_generator import generate_message

from kafka import KafkaProducer


# Mensagem precisam ser serializadas
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)



if __name__ == '__main__':
    while True:
        # Gera mensagem
        dummy_message = generate_message()
        # Envia ao tópico
        print(f'Mensagem produzida {datetime.now()} | Mensagem {str(dummy_message)}')
        producer.send('messages', dummy_message)

        # Sleep - tempo entre os envios        
        time.sleep(2)