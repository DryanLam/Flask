class DevelopmentConfig(object):
    # all config: https://flask.palletsprojects.com/en/1.1.x/config/
    ENV = 'development' #production
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE='Lax'
    MYSQL_DATABASE_USER = 'test'
    MYSQL_DATABASE_PASSWORD = 'test'
    MYSQL_DATABASE_DB = 'tadp'
    MYSQL_DATABASE_HOST = 'localhost'