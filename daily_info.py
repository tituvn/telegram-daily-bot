import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
AQI_TOKEN = "YOUR_AQI_TOKEN"
CITY = "hanoi"

# Get AQI
url = f"https://api.waqi.info/feed/{CITY}/?token={AQI_TOKEN}"
data = requests.get(url).json()

if data["status"] != "ok":
    raise Exception("AQI API error")

aqi = data["data"]["aqi"]
city_name = data["data"]["city"]["name"]

message = f"🌫 AQI Report\nCity: {city_name}\nAQI: {aqi}"

send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(send_url, json={
    "chat_id": CHAT_ID,
    "text": message
})
