import requests
from twilio.rest import Client
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_para = {
    "lat" :25.026219457235783,
    "lon" :121.41909206086044,
    "appid" : "a44068740825277d74e1b162dd339228",
    "cnt":4
}


account_sid = 'ACd11092e137f2ff13a9c4db07c53014d1'
auth_token = '94d95cd43dd2fd03f432a5ecaf3e35c1'

# recover code : 7LMNMH65ADNDZ2HVNM1UG8PM
# api key

response = requests.get(endpoint, params=weather_para)
response.raise_for_status()
data = response.json()  # 如果不加上json() ，會得出 <Response [200]>
will_rain = False
for n in data["list"]:
    if n["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body = "rain alert",
    from_='+12513095591',
    to='+8860908296150')
    print(message.status)