from kafka import KafkaConsumer

class MyKafkaConsumer:

    def __init__(self, topics : list[str], configs : dict) -> None:
        self.topics = topics
        self.configs = configs
        self.consumer = None


    def open(self):
        try:
            self.consumer = KafkaConsumer(*self.topics, **self.configs)
        except Exception as e:
            print(type(e).__name__, "-", e)
            raise RuntimeError(f"Kafka connect failed: {type(e).__name__} - {e}") from e


    def close(self):
        if self.consumer:
            self.consumer.close()


    def consume(self):
        for msg in self.consumer:
            yield msg