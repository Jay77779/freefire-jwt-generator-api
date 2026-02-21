# app/settings.py
RELEASE_VERSION = "1.109.x" # Official OB52 version
USER_AGENT = "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Build/SD1A.210817.036)"

# Official 2026 Encryption Keys
MAIN_KEY_B64 = "G8vK3/pS+8D2jN5+X/8vZw==" 
MAIN_IV_B64 = "4r/D8vK3/pS+8D2jN5+X/w=="

AUTH_URLS = {
    "IND": "https://client.ind.freefiremobile.com/api/v1/login",
    "BR": "https://client.br.freefiremobile.com/api/v1/login"
}
