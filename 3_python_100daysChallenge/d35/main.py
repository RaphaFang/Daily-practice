# api key
api_key = "a44068740825277d74e1b162dd339228"
# 25.026219457235783, 121.41909206086044
import requests
url = f"https://api.openweathermap.org/data/2.5/weather?lat={25.026219457235783}&lon={121.41909206086044}&appid={api_key}"
response = requests.get(url)
response.raise_for_status()  #reply if there is an http error
data = response.json()
print(data)

# print(response)
