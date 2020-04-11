from flask import Flask, request, make_response, Blueprint
import secrets
import json
import uuid

def data_res(injson):
	return make_response(json.dumps(injson,ensure_ascii=False).encode('utf-8'))

def createToken():
	preLengh = 7
	preToken = str(uuid.uuid4().hex)[:preLengh]
	sufToken = secrets.token_hex(16).upper()
	return f'{preToken}-{sufToken}'