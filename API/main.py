from views import app
import os

# app = Flask(__name__)
port = int(os.environ.get("API_PORT", 3500))

if __name__ == "__main__":
    app.config.from_object('config.DevelopmentConfig')
    app.run(debug=True,host='0.0.0.0',port=port)
    # app.run(debug=True, port=port)
    