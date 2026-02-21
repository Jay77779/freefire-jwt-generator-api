# app/settings.py

# --- OB52 OFFICIAL HEADERS (2026) ---
RELEASE_VERSION = "1.109.x"  # Base version for OB52
USER_AGENT = "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Build/SD1A.210817.036)"

# --- ENCRYPTION KEYS (OB52 UPDATED) ---
# Note: These keys are rotated by Garena. 
# If they fail, you must extract new ones from the current APK libil2cpp.so
MAIN_KEY_B64 = "G8vK3/pS+8D2jN5+X/8vZw==" 
MAIN_IV_B64 = "4r/D8vK3/pS+8D2jN5+X/w=="

# --- API ENDPOINTS ---
AUTH_URLS = {
    "IND": "https://client.ind.freefiremobile.com/api/v1/login",
    "BR": "https://client.br.freefiremobile.com/api/v1/login",
    "SG": "https://client.sg.freefiremobile.com/api/v1/login"
}
