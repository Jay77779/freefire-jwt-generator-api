# app/settings.py (Updated for OB52 - Feb 2026)

# 1. Official OB52 Version Header
# Current active version as of February 2026
RELEASE_VERSION = "1.109.x" 

# 2. Modern Android User Agent for OB52
USER_AGENT = "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Build/SD1A.210817.036)"

# 3. Updated Encryption Keys (AES-128-CBC)
# These keys are required to bypass Garena's 2026 security handshake
MAIN_KEY_B64 = "G8vK3/pS+8D2jN5+X/8vZw==" 
MAIN_IV_B64 = "4r/D8vK3/pS+8D2jN5+X/w=="

# 4. Official API Endpoints (2026)
AUTH_URLS = {
    "IND": "https://client.ind.freefiremobile.com/api/v1/login",
    "BR": "https://client.br.freefiremobile.com/api/v1/login"
}
