from flask import Flask
from views.login.login import login_blp
from views.query.query import query_blp
# from query import query_blp

app = Flask(__name__, static_folder="../static", template_folder="../templates")
# Blueprint need secret key to link app
app.secret_key = 'sadfuwhkanflk'

app.register_blueprint(login_blp)
app.register_blueprint(query_blp)