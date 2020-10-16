from flask import Flask, request, make_response, Blueprint
import secrets
import json
import uuid
import redis

def data_res(injson):
	return make_response(json.dumps(injson,ensure_ascii=False).encode('utf-8'))


def createToken():
	preLengh = 4
	preToken = str(uuid.uuid4().hex)[:preLengh].upper()
	sufToken = secrets.token_hex(16).upper()
	return f'{preToken}-{sufToken}'


def isTokenExpired(token):
    r = redis.Redis("localhost")
    return r.exists(token) == 0


def addRedisToken(token, data):
    r = redis.Redis("localhost")
    r.setex(token, 60*5, data)


def delRedisToken(token):
    r = redis.StrictRedis("localhost")
    r.delete(token)
 





