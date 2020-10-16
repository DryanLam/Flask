from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/tadp"
client = MongoClient(conn_str)
db = client.get_database('tadp')

coll = db.get_collection('inventory')

doc = {"name": "iPhone 12 Pro", "price": 999}
coll.insert_one(doc)



