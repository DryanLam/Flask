from flask import Flask, session, request, render_template, redirect, url_for
from flaskext.mysql import MySQL
from datetime import timedelta
import os
from utils import common


app = Flask(__name__, static_folder = '../static', template_folder="../templates")
app.config.from_object('config.DevelopmentConfig')
app.secret_key = os.urandom(16)
app.permanent_session_lifetime = timedelta(minutes=5)

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

            
@app.before_request
def require_oauth():
    if 'Login' not in request.endpoint and 'Register' not in request.endpoint:
        if 'token' in session:
            isExpired = common.isTokenExpired(session['token'])
            if isExpired:
                return redirect(url_for('login_blp.getLogin'))


@app.errorhandler(Exception)
def app_error_handle(e):
    return "There is an error. Please check your request or contact to admin. Thanks."


@app.errorhandler(404)
def page_not_found(error):
    return f"Page not found{request.path}"