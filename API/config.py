class DevelopmentConfig(object):
    ENV = 'development' #production
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE='Lax'
