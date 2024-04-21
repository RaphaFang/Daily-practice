# ------------------------------------------------------------------------------------------------------------------------------
# 可以運作，但是讀到的是未登入的頁面
# ------------------------------------------------------------------------------------------------------------------------------
# pip install zenrows
from zenrows import ZenRowsClient
import html

client = ZenRowsClient("89046282b1402b11fe09b238bcb8a580acebe6bf")
url = "https://www.zeczec.com/users/sign_in"
params = {"premium_proxy":"true","proxy_country":"tw","antibot":"true", "premium_proxy":"true",  "js_render":"true",}

response = client.get(url, params=params) #.decode()

print(response.text)