from flask import Flask, request, make_response, Blueprint
import secrets
import json
import uuid
import redis
from pymongo import MongoClient

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
 

def mongoFindOne(db,coll,filter={}):
    conn_str = "mongodb://localhost:27017/tadp"
    client = MongoClient(conn_str)
    db = client.get_database(db)
    coll = db.get_collection(coll)
    
    # data = coll.find_one({},{'_id': 0})
    data = coll.find_one(filter,{'_id': 0})
    return data


def mongoFindMany(db,coll,filter={}):
    conn_str = "mongodb://localhost:27017/tadp"
    client = MongoClient(conn_str)
    db = client.get_database(db)
    coll = db.get_collection(coll)
    
    data = []
    cursor = coll.find(filter,{'_id': 0})
    for doc in cursor:
        data.append(doc)
    return data


def mongoInsertOne(db,coll,data):
    try:
        conn_str = "mongodb://localhost:27017/tadp"
        client = MongoClient(conn_str)
        db = client.get_database(db)
        coll = db.get_collection(coll)
        coll.insert_one(data)
        return {"status": "success", "action": "insert", "data": data}
    except:
        return {"status": "false", "action": "insert", "data": data}


def mongoUpdateOne(db,coll,data):
    try:
        conn_str = "mongodb://localhost:27017/tadp"
        client = MongoClient(conn_str)
        db = client.get_database(db)
        coll = db.get_collection(coll)
        coll.update_one(data, {"$set": data}, upsert=True)              # upsert help to create if not exist and update for current value
        
        return {"status": "success", "action": "insert", "data": data}
    except:
        return {"status": "false", "action": "insert", "data": data}