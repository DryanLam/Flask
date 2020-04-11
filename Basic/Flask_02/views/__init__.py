from flask import Flask

app = Flask(__name__, static_folder="../static", template_folder="../templates")
# Blueprint need secret key to link app
app.secret_key = 'sadfuwhkanflk'


from views.login import login_blp
from views.query import query_blp

app.register_blueprint(login_blp)
app.register_blueprint(query_blp)