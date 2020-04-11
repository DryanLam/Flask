from flask import Flask, request, make_response, Blueprint
import secrets
import json
import uuid

login_blp = Blueprint('login_blp', __name__)

@login_blp.route("/hello")
def hello():
	prelengh = 7
	return make_response(str(uuid.uuid4().hex)[:prelengh])

@login_blp.route("/api/login", methods=['POST'])
def login():
	usrname = request.form.get('username')
	passwd = request.form.get('password')
	isLogin = False
	if isLogin:
		token = createToken()
		return data_res({"success": isLogin, 'token': token})
	else:
	 	return data_res({"success": False, "username": usrname})

def data_res(injson):
	return make_response(json.dumps(injson,ensure_ascii=False).encode('utf-8'))

def createToken():
	preLengh = 7
	preToken = str(uuid.uuid4().hex)[:preLengh]
	sufToken = secrets.token_hex(16).upper()
	return f'{preToken}-{sufToken}'