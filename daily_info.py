import requests

BOT_TOKEN = "8594042290:AAH1Z51z-e3tjL2tVfjsDIdS0aebvjDNxfE"
CHAT_ID = "8594042290"
AQI_TOKEN = "7872308c-03a3-4b21-b4a6-5e11f4c49980"
CITY = "hanoi"

aqi_url = f"https://api.waqi.info/feed/{CITY}/?token={AQI_TOKEN}"
resp = requests.get(aqi_url, timeout=20)
data = resp.json()

if data.get("status") != "ok":
    raise SystemExit(f"AQI API failed: {data}")

aqi = data["data"]["aqi"]
city_name = data["data"]["city"]["name"]

# =========================
# FORMAT MESSAGE
# =========================
message = (
    "🌫 DAILY AIR QUALITY REPORT\n"
    f"📍 Location: {city_name}\n"
    f"📊 AQI: {aqi}\n\n"
    "Stay safe ❤️"
)

# =========================
# SEND TO TELEGRAM
# =========================
tg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
res = requests.post(
    tg_url,
    json={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    },
    timeout=20
)

if res.status_code != 200:
    raise SystemExit(f"Telegram API error: {res.text}")

print("Message sent successfully ✅")
