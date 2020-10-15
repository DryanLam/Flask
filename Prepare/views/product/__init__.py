from views import curs, conn
from views import curs, conn
from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

product_blp = Blueprint('product_blp', __name__)

# @app.route('/reg', methods = ['GET'])
@product_blp.route('/product', methods = ['GET'])
def getProduct():
    return render_template('product.html')
    # if 'email' in session:
    #     return redirect(url_for('index_blp.index'))
    # else:
    #     return render_template('product.html')

