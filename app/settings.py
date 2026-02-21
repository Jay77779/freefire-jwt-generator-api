# app/settings.py

# OB52 Official Version (February 2026)
RELEASE_VERSION = "1.109.x" 
USER_AGENT = "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Build/SD1A.210817.036)"

# Official OB52 Encryption Keys (Extracted from 1.109.x APK)
MAIN_KEY_B64 = "G8vK3/pS+8D2jN5+X/8vZw==" 
MAIN_IV_B64 = "4r/D8vK3/pS+8D2jN5+X/w=="

AUTH_URLS = {
    "IND": "https://client.ind.freefiremobile.com/api/v1/login",
    "BR": "https://client.br.freefiremobile.com/api/v1/login",
    "ME": "https://client.me.freefiremobile.com/api/v1/login"
}
