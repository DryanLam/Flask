from flask import Flask
from products.login.login import login_blp
from products.query.query import query_blp
# from query import query_blp

app = Flask(__name__)
# Blueprint need secret key to link app
app.secret_key = 'sadfuwhkanflk'

app.register_blueprint(login_blp, url_prefix='/api')
app.register_blueprint(query_blp, url_prefix='/api/query')

@app.before_request
def require_authorization():
    isTokenExpired = False
    if not isTokenExpired:
        return "Token has been expired. Please re-authenticate!"

    # from flask import request
    # from flask.ext.login import current_user

    # if not (current_user.is_authenticated or request.endpoint == 'login'):
        # return login_manager.unauthorized()
