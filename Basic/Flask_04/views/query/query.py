from flask import Flask, request, make_response, Blueprint
import json

query_blp = Blueprint('query_blp', __name__)

# GET: params get from arg >> request.arg.get('username')
@query_blp.route("/api/user/<username>", methods=['GET'])
def findName(username):
	return make_response(json.dumps({"user": username, "id": 1}))