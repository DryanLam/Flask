# Create table
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect

metadata = MetaData()
books = Table('book', metadata,
  Column('id', Integer, primary_key=True),
  Column('title', String),
  Column('primary_author', String),
)

engine = create_engine('sqlite:///bookstore.db')
# engine = create_engine('postgresql://user:password@host/database')
metadata.create_all(engine)

# Inspect
inspector = inspect(engine)
inspector.get_columns('book')




# Insert by text with multiple data

from sqlalchemy.sql import text
with engine.connect() as con:

    data = ( { "id": 1, "title": "The Hobbit", "primary_author": "Tolkien" },
             { "id": 2, "title": "The Silmarillion", "primary_author": "Tolkien" },
    )

    statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")

    for line in data:
        con.execute(statement, **line)
        
        
# Then query
with engine.connect() as con:

    rs = con.execute('SELECT * FROM book')

    for row in rs:
        print row



# -----------------------------
# Database manager - Idea for multi-connector
https://medium.com/opex-analytics/database-connections-in-python-extensible-reusable-and-secure-56ebcf9c67fe



# -----------------------------
# Variable from Jinja2 form
<HTML>
<BODY bgcolor="cyan">
<form method="POST" action="">
    <center>
    <H1>Enter your details </H1> <br>
    First Name <input type = "text" name= "fname" /> <br>
    Last Name <input type = "text" name = "lname" /> <br>
    <input type = "submit">
    </center>
</form>
</BODY>
</HTML>

#---
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
      if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
      return render_template('index.html')

if __name__ == '__main__':
    app.run()
    
# ----------------------------- REDIS
import redis

# r = redis.Redis("localhost", port=6379)
r = redis.Redis("localhost")        # Default listen all port 6379
v = r.get("name")
print(v)

print(r.set("tadp","microservices"))
print(r.set("count",1))



# ----------------------------- MONGODB
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