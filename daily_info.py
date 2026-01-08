import requests

BOT_TOKEN = "8594042290:AAH1Z51z-e3tjL2tVfjsDIdS0aebvjDNxfE"
CHAT_ID = "8594042290"
AQI_TOKEN = "7872308c-03a3-4b21-b4a6-5e11f4c49980"
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
