from flask import Flask, request, make_response, Blueprint
import json

query_blp = Blueprint('query_blp', __name__)

# GET: params get from arg >> request.arg.get('username')
@query_blp.route("/user/<username>", methods=['GET'])
def findName(username):
	return make_response(json.dumps({"user": username}))

@query_blp.route("/user/sample", methods=['GET'])
def userSample():
	return make_response(json.dumps({"user": "sample"}))