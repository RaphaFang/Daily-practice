# import urllib.request as request
# import bs4
# import json

# url = "https://www.zeczec.com/"
# req = request.Request(
#     url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
# )
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
# >>>> header 加上後面的作業系統，反而不讓進？


# # data = request.urlopen(req).read()
# with request.urlopen(req) as data:
#     data = json.load(data)

# with request.urlopen(req) as response:
#     webpage = bs4.BeautifulSoup(response.read().decode('utf-8'), features="html.parser")
# print(webpage)
# ------------------------------------------------------------------------------------------------------------------------------
# >>>> urllib.request 只能爬靜態的網頁，沒辦法作動態有js或是有阻擋的網頁。即便你的header有修改也一樣


# ------------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.chrome.options import Options
from zenrows import ZenRowsClient

client = ZenRowsClient("89046282b1402b11fe09b238bcb8a580acebe6bf")
url = "https://www.zeczec.com/users/sign_in"
params = {"premium_proxy":"true","proxy_country":"tw"}

response = client.get(url, params=params)

url = "https://www.zeczec.com/users/sign_in"
driver = webdriver.Chrome()
driver.get(url)

email_blank = driver.find_element("id", "user_email")
email_blank.send_keys("nickmomo1524@gmail.com")
time.sleep( 10 )
password_blank = driver.find_element("id", "user_password")
password_blank.send_keys("1aqzwx2s")
time.sleep( 8 )
button = driver.find_element("name","commit")
button.click()
# driver.implicitly_wait(5)
time.sleep(10 )
check_button = driver.find_element(By.XPATH,"//input[@type='checkbox']")  #find_element("type","checkbox")
check_button.click()
time.sleep( 15 )
time.sleep( 15 )


# driver.implicitly_wait(10) # seconds

# driver.save_screenshot("test.png")




print(response.text)


# ------------------------------------------------------------------------------------------------------------------------------
# selenium 已經更新了，所以一些就無張的func 不會work
#         https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el