
# config.py
# --- Edit these values before running ---

# Telegram Bot settings
BOT_TOKEN = "8150043265:AAG1_5sWNuRPfjBqg8i328XhSLTi3olt19c"
ADMIN_ID = 6958805951
GROUP_ID = -1002640997198
OWNER_LINK = "Https://t.me/msmahidtech"
CHANNEL_LINK = "https://t.me/AllOtpReceiver"


# ==========================================================
# IVASMS Login Credentials
# ==========================================================
LOGIN_URL = "https://www.ivasms.com/login"
LOGIN_EMAIL = "msgemssp@gmail.com"
LOGIN_PASSWORD = "mahfuz63@63"

# IVASMS endpoints
BASE = "https://www.ivasms.com"
GET_SMS_URL = f"{BASE}/portal/sms/received/getsms"
GET_NUMBER_URL = f"{BASE}/portal/sms/received/getsms/number"
GET_OTP_URL = f"{BASE}/portal/sms/received/getsms/number/sms"

# ==========================================================
# Session and CSRF token (leave these as they are)
# ==========================================================
SESSION_COOKIE = "cf_clearance=MLLiyNNk5fHnw.UKvMmqbtuYV3UY0xP7vSE0iHIxgSs-1761192118-1.2.1.1-os5cyMog9.psjE_LFpzav9X4ptlWEwvg.eX1F8qOrGN4chh61Bq9BNvXnCt9kWlEpQ77yQCu2X0uM34XuzLwCeQsHhdbtSxY.0nAHAJjxwmeE55jtIjHrx2zWGpVD27LOfrhZdwStANsyUTl79RXKfptKFPb9GaW62FcZjGZoCKkW34h2Sw0EhCeVVIAWUvsgxPSxNFoXfrNOq3akMPmVgEzr4Y_CovoShlIU4D22Ic; XSRF-TOKEN=eyJpdiI6IlNpMzRHMVZWcEsrRTAySVJST1hOY3c9PSIsInZhbHVlIjoieGMzMHJ6QzZZclFwdStTbldBaDdhcitQMHJ1S0RQKzEyWUJPWGxBRnpBNjVJa1h2QUtuYStnYWJtRmtHbk43d1NWUUhzczdPZERlbCtMMlRhUkhZeUZvUjBKcEYySzREb3Vneit1V0VLZ0ZMSGZPbnZBdERvK2ZRYXhmOW1sWmciLCJtYWMiOiIzMjAyY2I5OGUxNDkzOTgzNDYzNWNmODZkMWNjYTVmZDJkM2MzZGUxMmY0ZWQ3MTNmZDM1MDI0ZTgwYTk5ODc0IiwidGFnIjoiIn0%3D; ivas_sms_session=eyJpdiI6IjFxcTVJZXlxZStBL0hXb2ZzMnlxZEE9PSIsInZhbHVlIjoiRCtVbk5VUW5Lc3h4eEdXb215R2dneHdOUTRCTGpZRnlFNS9UMVlqR2VrSlh1NkkxYVRQSGl3Y1M1OHNWYjJFc0JMWWNCbVgzTzJ0SitKcDBnZmNMbFlKb3R4czRuSVdCRGFOMTNWL0VobnJyUGp1dk1SbEFENG1EOXE0eUN2RmkiLCJtYWMiOiI0OTA5NTAyZjRhNWM5NzVmYTViNDlkMjdhYTg1YTc2YzgxNmJiODA2Y2E5NjBjMjE2MzQxMGM2NDUyNjc5Y2FmIiwidGFnIjoiIn0%3D; _fbp=fb.1.1761192130154.223012430810351080"
CSRF_TOKEN = "4Wt8YmDtZzlTjI151IDM0LGqtPIwlF8z3VsYthpQ"

# Request headers (don't change unless necessary)
HEADERS = {
    "Origin": "https://www.ivasms.com",
    "Referer": "https://www.ivasms.com/portal/sms/received",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}

# Polling interval (seconds)
FETCH_INTERVAL = 6

# DB file
DB_FILE = "otps_and_errors.db"
# ==========================================================
# Country and Service Mappings
# ==========================================================
COUNTRY_FLAGS = {
    "234": "🇳🇬 Nigeria",
    "880": "🇧🇩 Bangladesh",
    "51": "🇵🇪 Peru",
    "225": "🇨🇮 Ivory Coast",
    "20": "🇪🇬 Egypt",
    "255": "🇹🇿 Tanzania",
    "44": "🇬🇧 United Kingdom",
    "58": "🇻🇪 Venezuela",
    "996": "🇰🇬 Kyrgyzstan",
    "593": "🇪🇨 Ecuador",
    "591": "🇧🇴 Bolivia",
    "228": "🇹🇬 Togo",
    "221": "🇸🇳 Senegal",
    "1": "🇺🇸 United States",
    "970": "🇵🇸 Palestine",
    "98": "🇮🇷 Iran",
    "964": "🇮🇶 Iraq",
    "966": "🇸🇦 Saudi Arabia",
    "236": "🇨🇫 Central African Republic",
    "93": "🇦🇫 Afghanistan",
    "261": "🇲🇬 Madagascar",
    "977": "🇳🇵 Nepal",
    "967": "🇾🇪 Yemen",
    "998": "🇺🇿 Uzbekistan",
    "216": "🇹🇳 Tunisia",
    "963": "🇸🇾 Syria",
    # Sabbin Ƙasashe
    "229": "🇧🇯 Benin",
    "63": "🇵🇭 Philippines",
    "60": "🇲🇾 Malaysia",
    "992": "🇹🇯 Tajikistan",
    "254": "🇰🇪 Kenya"
}

# An ƙara wasu kalmomi don gane sabis da kyau
SERVICES = {
    "whatsapp": "WhatsApp",
    "facebook": "Facebook",
    "meta": "Facebook",
    "fb": "Facebook",
    "telegram": "Telegram",
    "google": "Google",
    "instagram": "Instagram",
    "signal": "Signal",
    "snapchat": "Snapchat",
    "tiktok": "Tiktok",
    "twitter": "Twitter",
    "premierbet": "Premier Bet",
    "premier bet": "Premier Bet",
    # Sabbin Ayyuka
    "truecaller": "Truecaller",
    "netflix": "Netflix",
    "microsoft": "Microsoft",
    "binance": "Binance",
    "twilio":  "Twilio"
}

# Masking rule: keep first N chars then **** then last M chars
MASK_PREFIX_LEN = 7
MASK_SUFFIX_LEN = 3
