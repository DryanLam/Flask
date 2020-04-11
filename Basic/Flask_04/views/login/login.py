from flask import Flask, request, make_response, Blueprint
import secrets
import json
import uuid

from utils import common

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
		token = common.createToken()
		return common.data_res({"success": isLogin, 'token': token})
	else:
	 	return common.data_res({"success": False, "username": usrname})