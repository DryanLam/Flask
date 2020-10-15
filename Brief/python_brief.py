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
    
# -----------------------------