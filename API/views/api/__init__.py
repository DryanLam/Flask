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


@api_blp.route('/order', methods = ['GET'])
def orders():
    user = request.args.get('user')
    _db = "tadp"
    _coll = "order"
    _filter = {"user": user}
    rs = common.mongoFindOne(_db,_coll, _filter)
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
    _coll = "inventory"
    data = {"name": "iPhone 12 Pro", "cost": 999, "url": "https://www.apple.com/newsroom/images/product/iphone/standard/apple_iphone-12_new-design_10132020.jpg.landing-big_2x.jpg"} 
    rs = common.mongoUpdateOne(_db,_coll,data)
    return jsonify(str(rs))


# curl -i -H "Content-Type: application/json" -d '{"user": "Dung", "amt": 1, "cost": 999}' -X POST localhost:3500/api/v1/order
# curl -i -H "Content-Type: application/json" -H "Token: name"  -X GET localhost:3500/api/v1/order?user=abc@gmail.com
# curl -i -H "Content-Type: application/json" -H "Token: name" -d '{"user": "Dung", "amt": 1, "cost": 999}' -X POST localhost:3500/api/v1/order
# curl -i -H "Content-Type: application/json" -H "Token: name" -d '{"user": "Dung", "amt": 1, "cost": 999}' -X GET localhost:3500/api/v1/test