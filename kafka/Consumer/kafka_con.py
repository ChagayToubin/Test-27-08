from kafka import KafkaConsumer

class KafkaDAL:

    def __init__(self, configs):
        self.configs = configs
        self.consumer = None

    def open(self):
        try:
            self.consumer = KafkaConsumer(**self.configs)
        except Exception as e:
            print(type(e).__name__, "-", e)
            raise RuntimeError("Failed to connect to Kapka.") from e

    def close(self):
        if self.consumer:
            self.consumer.close()

    def consume_forever(self):
        for ms in self.consumer:
            yield ms