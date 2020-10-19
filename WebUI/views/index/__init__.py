from views import curs
from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from utils import common


index_blp = Blueprint('index_blp', __name__)

@index_blp.route('/', methods = ['GET'])
def index():
    if 'token' in session:
        # _sessionemail = session['email']
        pd_img = common.getProduct()
        return render_template('index.html', price=common.getPrice(), url_pd = pd_img)
    else:
        return redirect(url_for('login_blp.getLogin'))


@index_blp.route('/', methods = ['POST'])
def doOrder():
    # _user = session['email']
    # _price = common.getPrice()
    # _cost = _qty  * _price
    # data = {}
    # data['qty'] = int(request.form["quantity"])
    # data['cost'] = _qty  * common.getPrice()
    
    _qty = int(request.form["quantity"])
    common.doOrder({'qty': _qty, 'cost': _qty  * common.getPrice()})
    
    return redirect(url_for('index_blp.getOrder'))
    # return redirect(url_for('index_blp.getOrder', user=_user, qty=_qty, price=_price, cost=_cost))
    # return render_template('order.html', user=_user, qty=_qty, price=_price, cost=_cost)


@index_blp.route('/order', methods = ['GET'])
def getOrder():
    # _user=request.args.get('user')
    # _qty=request.args.get('qty')
    # _price=request.args.get('price')
    # _cost=request.args.get('cost')
    print('start get order------------------------')
    data = common.getOrder()
    pd_img = common.getProduct()
    
    return render_template('order.html',user = data['user'], qty = data['amt'], price = data['cost']/data['amt'], cost = data['cost'], url_pd = pd_img)