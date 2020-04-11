from flask import Flask, request, make_response, Blueprint
import secrets
import json
import uuid

from utils import common

# login_blp = Blueprint('login_blp', __name__, static_folder='static', static_url_path='login')
login_blp = Blueprint('login_blp', __name__, static_folder='static', template_folder='templates')

@login_blp.route("/hello")
def hello():
	prelengh = 7
	return make_response(str(uuid.uuid4().hex)[:prelengh])

@login_blp.route("/login", methods=['POST'])
def login():
	usrname = request.form.get('username')
	passwd = request.form.get('password')

	isLogin = '123456' == passwd
	if isLogin:
		token = common.createToken()
		return common.data_res({"success": isLogin, 'token': token})
	else:
	 	return common.data_res({"success": False, "username": usrname})