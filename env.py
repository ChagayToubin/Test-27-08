import os

HOST = os.getenv("HOST", "cluster0.6ycjkak.mongodb.net")
USER = os.getenv("USER", "IRGC_NEW")
PASSWORD = os.getenv("PASSWORD", "iran135")
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "tweets")

# mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/