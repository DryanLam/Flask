from views import curs
from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from utils import common


login_blp = Blueprint('login_blp', __name__)


@login_blp.route('/login', methods=['GET'])
def getLogin():
    if 'token' in session:
        if common.isTokenExpired(session['token']):
            return render_template('login.html')
        return redirect(url_for('index_blp.index'))
    else:
        return render_template('login.html')


@login_blp.route('/login', methods=['POST'])
def postLogin():
    try:
        errors = []
        _email = request.form.get('inputEmail', None)
        _password = request.form.get('inputPassword', None)
        sql = "SELECT password FROM tbl_users WHERE EMAIL = '{0}'".format(_email)
        curs.execute(sql)
        rows = curs.fetchone()
        hashedpassword = rows[0]
        if rows and check_password_hash(hashedpassword, _password):
            # session.permanent = True          # This option will keep session until logout
            _token = common.createToken()
            print("Token: " + _token)
            session['email'] = _email
            session['token'] = _token
            print("Set token to Redis")
            common.addRedisToken(_token, _email)
            print(request.endpoint)             # login_blp.postLogin
            
            return redirect(url_for('index_blp.index'))
        else:
            errors.append("Username and password are not found.")
            return render_template('login.html', errors=errors)
    except Exception as e:
        raise(e)
        pass

@login_blp.route('/logout', methods = ['GET'])
def getLogout():
    common.delRedisToken(session['token'])
    session.pop('email', None)
    session.pop('token', None)
    
    return redirect(url_for('index_blp.index'))