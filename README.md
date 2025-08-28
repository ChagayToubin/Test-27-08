# Malicious Text Feature Engineering System V2

This project uses **Kafka** and **MongoDB** to process and store text data.  
The idea is to pull text messages from a database, clean them, add some extra features, and then save them into a local MongoDB.  
There is also a small API service to fetch the processed data.

## Services
- **Retriever** – fetches data from MongoDB Atlas and sends it to Kafka.  
- **Preprocessor** – cleans the text (remove symbols, lowercase, stop words, etc.) and publishes it back.  
- **Enricher** – adds more features like sentiment, weapons detection, and dates.  
- **Persister** – saves everything into the local MongoDB (two collections: antisemitic and not antisemitic).  
- **DataRetrieval** – simple API to return the data.

## How to run
1. Start Kafka and MongoDB locally:
   ```bash
   docker run -d --name kafka -p 9092:9092 apache/kafka
   docker run -d --name mongo -p 27017:27017 mongo
