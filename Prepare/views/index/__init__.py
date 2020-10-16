from views import curs
from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

index_blp = Blueprint('index_blp', __name__)

@index_blp.route('/', methods = ['GET'])
def index():
    _price = 999
    if 'email' in session:
        _sessionemail = session['email']
        return render_template('index.html',price=_price)
    else:
        return redirect(url_for('login_blp.getLogin'))


@index_blp.route('/', methods = ['POST'])
def doOrder():
    _user = session['email']
    _price = 999
    _qty = int(request.form["quantity"])
    _cost = _qty  * _price
    return redirect(url_for('index_blp.getOrder', user=_user, qty=_qty, price=_price, cost=_cost))
    # return render_template('order.html', user=_user, qty=_qty, price=_price, cost=_cost)


@index_blp.route('/order', methods = ['GET'])
def getOrder():
    _user=request.args.get('user')
    _qty=request.args.get('qty')
    _price=request.args.get('price')
    _cost=request.args.get('cost')
    return render_template('order.html',user=_user, qty=_qty, price=_price, cost=_cost)