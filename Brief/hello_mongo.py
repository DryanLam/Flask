from pymongo import MongoClient

conn_str = "mongodb://localhost:27017/tadp"
client = MongoClient(conn_str)


# List all databases
print(client.list_database_names())

# Get/create database to interact
db = client.get_database('tadp')
print(db.list_collection_names())


# Insert document to collection
# Single
col_01 = db.get_collection('store')
doc_01 = {"item": "canvas", "qty": 100, "tags": ["cotton"], "size": {"h": 20, "w": 10, "uom": "cm"}} 
col_01.insert_one(doc_01)


# Multiple
col_02 = db.get_collection('store')
doc_02 = []
doc_02.append({"item": "canvas", "qty": 100, "tags": ["cotton"], "size": {"h": 20, "w": 10, "uom": "cm"}} )
doc_02.append({"item": "journal", "qty": 50, "tags": ["blank", "red"], "size": {"h": 12, "w": 21, "uom": "cm"}} )
col_02.insert_many(doc_02)



# Find document
col_03 = db.get_collection('store')
doc_03 = col_03.find_one()
print(doc_03)

cursor_03 = col_03.find()
for doc in cursor_03:
    print(doc)


# Filter
col_04 = db.get_collection('store')
filter_04 = {"qty": 50}
cursor_04 = col_04.find(filter_04)
print(cursor_04.count())
for doc in cursor_04:
    print(doc)


# Find & sort
col_05 = db.get_collection('store')
cursor_05 = col_05.find().sort('qty',1)
for doc in cursor_05:
    print(doc)
cursor_06 = col_05.find().sort('qty',-1)
for doc in cursor_06:
    print(doc)


# Delect
# One
col_07 = db.get_collection('store')
result_07 = col_07.delete_one({"item": "canvas"})

# Many
col_08 = db.get_collection('store')
result_08 = col_08.delete_many({"item": "journal"})
print(result_08.deleted_count)


# Update
col_09 = db.get_collection('store')
col_09.update_one({"item": "canvas"}, {"$set": {"qty": 3}})
col_09.update_many({"item": "canvas"}, {"$set": {"qty": 3}})

count = col_09.count_documents({})
print(count)