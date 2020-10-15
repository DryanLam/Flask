from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__, static_folder = '../static', template_folder="../templates")
app.config['MYSQL_DATABASE_USER'] = 'test'
app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
app.config['MYSQL_DATABASE_DB'] = 'tadp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = 'sadfuwhkanflk'

# MySQL configurations
print("Initializing database connection!")
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
curs = conn.cursor()
print("Database connected!")


from views.index import index_blp
from views.login import login_blp
from views.register import register_blp
from views.product import product_blp

app.register_blueprint(index_blp)
app.register_blueprint(login_blp)
app.register_blueprint(register_blp)
app.register_blueprint(product_blp)