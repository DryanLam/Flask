from flask import Flask, url_for, render_template, request, render_template, make_response, session, escape, redirect
import secrets
import os
import json
import redis
import uuid

from views import app

app = Flask(__name__)

@app.route("/hello")
def hello():
	prelengh = 7
	return make_response(str(uuid.uuid4().hex)[:prelengh])

# GET: params get from arg >> request.arg.get('username')
@app.route("/api/user/<username>", methods=['GET'])
def findName(username):
	return make_response(json.dumps({"user": username, "id": 1}))

# POST: params get from form >> request.form.get('username')
# HEADER
# Form-data: curl -X POST -F "username=johndoe" -F "password=abcd1234" http://localhost:3000/api/login
# application/x-www-form-urlencoded: curl -d "username=johndoe&password=abcd1234" http://localhost:3000/api/login
# JSON: curl -X POST -H "Content-Type: application/json" -d '{"username":"johndoe", "password":"abcd1234"}' 

@app.route("/api/login", methods=['POST'])
def login():
	usrname = request.form.get('username')
	passwd = request.form.get('password')
	isLogin = False
	if isLogin:
		token = createToken()
		return data_res({"success": isLogin, 'token': token})
	else:
	 	return data_res({"success": False, "username": usrname})

# curl http://localhost:3000/api/check?token=12343
@app.route("/api/check", methods=['GET'])
def query():
	gtoken = request.args.get('token')
	return data_res({'token': gtoken, "isValid": True})






def createToken():
	preLengh = 7
	preToken = str(uuid.uuid4().hex)[:preLengh]
	sufToken = secrets.token_hex(16).upper()
	return f'{preToken}-{sufToken}'


def data_res(injson):
	return make_response(json.dumps(injson,ensure_ascii=False).encode('utf-8'))






# Sign key to Flask(Mandatory). Ablt to input any string
# app.secret_key = os.urandom(24)

# @app.route("/")
# def index():

# 	# Get cookie username
# 	var1 = request.cookies.get('username')

# 	# Session interaction
# 	if 'ldtsession' in session:
# 		print(escape(session['ldtsession']))
# 	else:
# 		session['ldtsession'] = 'sessionString'

# 	if 'email' in session:
# 		return redirect(url_for('index')) 

# 	# Render page
# 	pRender = render_template('kethua.html')
	
# 	# Cook reponse from page render
# 	resp = make_response(pRender)
# 	# Set cookie before return
# 	resp.set_cookie('abc','xyz','username','dryanlam')
# 	resp.set_cookie('username','dryanlam')
	
# 	return resp

# @app.route("/logout")
# def logOut():
# 	session.pop('email')
# 	return redirect(url_for('login'), code=302)



# @app.route("/user/<int:id>", methods=['GET','POST'])
# def findId(id):
# 	print("Method is " + request.method)
# 	return f"Hello {id} item(s)!"

# def getUsersFromRedis():
# 	import json
# 	import redis
# 	res = redis.StrictRedis(host='localhost',port='6379',db=0)
# 	users = json.loads(res.get('users'))
# 	return users

# def checkLogin(username,password):
# 	users = getUsersFromRedis()
# 	user = [user for user in users if user['username'] = username]
# 	if(len(user) > 0 and user[0]['password'] == password):
# 		return True
# 	else:
# 		return False

# def saveToken(username, token, expire_time = 30*60):
# 	import redis
# 	res = redis.StrictRedis(host='localhost',port='6379',db=0)
# 	res.setex(f"{username}_token", expire_time, token)
# 	return True

# @app.route("api/user/login", methods=['POST'])
# def doLogin(){
# 	username = request.form.get('username')
# 	password = request.form.get('password')
# 	if checkLogin(username,password):
# 		from secret import token_hex 
# 		utoken = token_hex(16)
# 		saveToken(username,utoken)
# 		import json
# 		return make_response(json.dumps({'result':True,'token':utoken}))
# 	else:
# 		return make_response(json.dumps({'result':False}))
# }

# def checkToken(username,toke):
# 	res = redis.StrictRedis(host='localhost',port='6379',db=0)
# 	gtoken = res.get(f"{username}_token")
# 	if gtoken == token.encode('UTF-8'):
# 		return True
# 	else:
# 		return False


# @app.route("api/users", methods=['GET'])
# def getUser():
# 	username = request.args.get('username')
# 	token = request.args.get('token')
# 	if checkToken(username,token):
# 		result = {'result':True, 'users':getUsersFromRedis()}
# 		return make_response(json.dumps(result))
# 	else:
# 		return make_response(json.dumps({'result':False}))


if __name__ == '__main__':
	app.run(debug=True)

# python3 main.py






