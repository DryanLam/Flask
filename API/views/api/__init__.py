from flask import request, Response, json, Blueprint, jsonify, abort
from utils import common

api_blp = Blueprint('api_blp', __name__)


@api_blp.route('/pricing', methods = ['GET'])
def pricing():
    _db = "tadp"
    _coll = "inventory"
    _filter = {"name": "iPhone 12 Pro"}
    rs = common.mongoFindOne(_db,_coll,_filter)
    return jsonify(rs)


@api_blp.route('/orders', methods = ['GET'])
def orders():
    _db = "tadp"
    _coll = "order"
    rs = common.mongoFindMany(_db,_coll)
    return jsonify(rs)


@api_blp.route('/order', methods = ['POST'])
def order():
    if not request.json or not 'user' in request.json:
        return abort(400)
    
    _db = "tadp"
    _coll = "order"
    # data = {"user": request.json['user'], "amt": request.json['amt'], "cost": request.json['cost']} 
    data = request.json 
    rs = common.mongoUpdateOne(_db,_coll,data)
    return jsonify(str(rs))


@api_blp.route('/test', methods = ['GET'])
def test():
    _db = "tadp"
    _coll = "order"
    data = {"user": "Dung", "amt": 1, "cost": 999} 
    rs = common.mongoUpdateOne(_db,_coll,data)
    return jsonify(str(rs))


# curl -i -H "Content-Type: application/json" -d '{"user": "Dung", "amt": 1, "cost": 999}' -X POST localhost:3500/api/v1/order
# curl -i -H "Content-Type: application/json" -H "Token: name" -d '{"user": "Dung", "amt": 1, "cost": 999}' -X POST localhost:3500/api/v1/order