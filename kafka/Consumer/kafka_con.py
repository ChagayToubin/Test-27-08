from kafka import KafkaConsumer

class KafkaDAL:

    def __init__(self, topics : list[str], configs : dict) -> None:
        self.topics = topics
        self.configs = configs
        self.consumer = None


    def open(self):
        try:
            self.consumer = KafkaConsumer(*self.topics, **self.configs)
        except Exception as e:
            print(type(e).__name__, "-", e)
            raise RuntimeError("Failed to connect to Kapka.") from e


    def close(self):
        if self.consumer:
            self.consumer.close()


    def consume(self):
        for msg in self.consumer:
            yield msg