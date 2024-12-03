from pymongo import MongoClient

# MongoDB URI
MONGO_URI = "mongodb+srv://bka2bg:QcqSyZpNSyiH52cU@crisismanagement.vypxy.mongodb.net/Crisis_Management"

# Connect to MongoDB and return the collection
def get_db():
    client = MongoClient(MONGO_URI)
    db = client.get_database()  # Automatically connects to the "Crisis_Management" DB
    return db.documents  # Replace 'documents' with your collection name
