import base64

class Settings:
    # Official OB52 Config
    RELEASE_VERSION = "1.109.x"
    X_UNITY_VERSION = "2022.3.17f1"
    USER_AGENT = "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Build/SD1A.210817.036)"
    TIMEOUT = 15.0

    # Keys (Must be bytes for core.py)
    MAIN_KEY = base64.b64decode("G8vK3/pS+8D2jN5+X/8vZw==")
    MAIN_IV = base64.b64decode("4r/D8vK3/pS+8D2jN5+X/w==")

    # Endpoints
    OAUTH_URL = "https://auth.garena.com/api/v1/login"
    MAJOR_LOGIN_URL = "https://client.ind.freefiremobile.com/api/v1/login"
    CLIENT_SECRET_PAYLOAD = "secret_value&client_id=100067"

# This line creates the "settings" object that core.py is trying to import
settings = Settings()
