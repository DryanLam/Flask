from flask import Flask, session, request, render_template, redirect, jsonify, make_response
import os
from utils import common


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.secret_key = os.urandom(16)


# Register blueprint
from views.api import api_blp
app.register_blueprint(api_blp, url_prefix='/api/v1')


@app.before_request
def require_oauth():
    if 'Token' not in request.headers:
        return make_response(jsonify({'error': 'Missing authentication'}), 404)
    else:
        _token = request.headers['Token']
        isExpired = common.isTokenExpired(_token)
        if isExpired:
            return make_response(jsonify({'error': 'Invalid session'}), 404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)