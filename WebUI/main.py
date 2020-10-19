from views import app
import os

# app = Flask(__name__)
port = int(os.environ.get("WEB_PORT", 3000))

if __name__ == "__main__":
    # debug = True to forece flask reload when code changed
    app.config.from_object('config.DevelopmentConfig')
    app.run(debug=True,host='0.0.0.0',port=port)