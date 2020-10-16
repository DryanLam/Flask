from flask import Flask, request

from utils import common

from products.login.login import login_blp
from products.query.query import query_blp

app = Flask(__name__)
# Blueprint need secret key to link app
app.secret_key = 'sadfuwhkanflk'

app.register_blueprint(login_blp, url_prefix='/api')
app.register_blueprint(query_blp, url_prefix='/api/query')

@app.before_request
def require_authorization():
    if "token" not in request.headers and '.login' not in request.endpoint:
        return "Invalid authentication"
    elif '.login' not in request.endpoint: 
        token = request.headers.get("token")
        print(token)
        isExpire = common.isTokenExpired(token)
        if isExpire:
            return "Token has been expired. Please re-authenticate!"

    # from flask import request
    # from flask.ext.login import current_user

    # if not (current_user.is_authenticated or request.endpoint == 'login'):
        # return login_manager.unauthorized()

@app.errorhandler(Exception)
def app_error_handle(e):
    # app.logger.error('Unhandled Exception: %s', (e))
    return "There is an error. Please check your request or contact to admin. Thanks."


@app.errorhandler()
def page_not_found(error):
    return f"Page not found{request.path}"