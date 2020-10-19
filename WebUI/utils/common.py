from flask import Flask, request, make_response, Blueprint, session
import secrets
import json
import uuid
import redis
import requests

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
 

def doGet(_url, _params, _headers={}):
    r = requests.get(url=_url, params=_params, headers=_headers) 
    data = r.json() 
    return data


def doPost(_url, _payload, _headers={}):
    r = requests.post(url=_url, data=json.dumps(_payload), headers=_headers) 
    data = r.json() 
    return data


def getPrice():
    end_point = "http://localhost:3500/api/v1/pricing"
    query = {}
    headers = {"Token": session['token'], "Content-Type": "application/json"}
    rs = doGet(end_point, query, headers)
    return rs['cost']


def getProduct():
    end_point = "http://localhost:3500/api/v1/pricing"
    query = {}
    headers = {"Token": session['token'], "Content-Type": "application/json"}
    rs = doGet(end_point, query, headers)
    return rs['url']


def doOrder(data):
    end_point = "http://localhost:3500/api/v1/order"
    payload = {"user": session['email'], "amt": data['qty'], "cost": data['cost']}
    headers = {"Token": session['token'], "Content-Type": "application/json"}
    rs = doPost(end_point, payload, headers)
    print(rs)
    

def getOrder():
    print('start get order method------------------------')
    end_point = "http://localhost:3500/api/v1/order?user=" + session['email']
    query = {}
    headers = {"Token": session['token'], "Content-Type": "application/json"}
    rs = doGet(end_point, query, headers)
    return rs