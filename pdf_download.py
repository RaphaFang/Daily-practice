# ------------------------------------------------------------------------------------------------------------------------------
# >>>> urllib.request 只能爬靜態的網頁，沒辦法作動態有js或是有阻擋的網頁。即便你的header有修改也一樣
# ------------------------------------------------------------------------------------------------------------------------------
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
# 爬網頁會阻擋，無法通過機器人測試
# 嘗試zenrows 這方法，https://www.zenrows.com/blog/selenium-stealth#limitations-and-alternatives
# 同時發現 selenium 已經更新了，所以一些舊文章的func 建議不會work
#         https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el
#         https://app.zenrows.com/builder
# ------------------------------------------------------------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # from zenrows import ZenRowsClient
# # client = ZenRowsClient("89046282b1402b11fe09b238bcb8a580acebe6bf")
# # url = "https://www.zeczec.com/users/sign_in"
# # params = {"premium_proxy":"true","proxy_country":"tw"}
# # response = client.get(url, params=params)

# url = "https://www.zeczec.com/users/sign_in"
# driver = webdriver.Chrome()
# driver.get(url)

# email_blank = driver.find_element("id", "user_email")
# email_blank.send_keys("nickmomo1524@gmail.com")
# # time.sleep( 10 )
# password_blank = driver.find_element("id", "user_password")
# password_blank.send_keys("1aqzwx2s")
# # time.sleep( 8 )
# button = driver.find_element("name","commit")
# button.click()
# # time.sleep(10)

# # check_button = driver.find_element(By.XPATH,"//input[@type='checkbox']")  #find_element("type","checkbox")
# # check_button.click()
# check_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
# check_button.click()

# time.sleep( 15 )



# ------------------------------------------------------------------------------------------------------------------------------
# 增加輸入等待時間，# check_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
# 也無法通過
# 發現連接家中wifi舊可以通過，但是手機熱點不行
# 透過修改ip / 使用中正vpn 都失敗，都過不了機器人測試，Cloudflare protection
# ------------------------------------------------------------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# import subprocess
# def set_static_ip(interface, ip_address, subnet_mask, router):
#     try:
#         # Configure the interface with the provided static IP address, subnet mask, and router
#         subprocess.check_output(f"sudo networksetup -setmanual {interface} {ip_address} {subnet_mask} {router}", shell=True)
#         print("Static IP address configured successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error configuring static IP address: {e}")

# # Example usage
# interface = "Wi-Fi"  # Replace with your interface name, e.g., "Wi-Fi" or "Ethernet"
# ip_address = "192.168.1.100"  # Replace with your desired IP address
# subnet_mask = "255.255.255.0"  # Replace with your subnet mask
# router = "192.168.1.1"  # Replace with your router IP address

# set_static_ip(interface, ip_address, subnet_mask, router)

# url = "https://www.zeczec.com/users/sign_in"
# driver = webdriver.Chrome()
# driver.get(url)

# email_blank = driver.find_element("id", "user_email")
# email_blank.send_keys("nickmomo1524@gmail.com")
# # # time.sleep( 10 )

# password_blank = driver.find_element("id", "user_password")
# password_blank.send_keys("1aqzwx2s")
# button = driver.find_element("name", "commit")
# button.click()

# check_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
# check_button.click()



# ------------------------------------------------------------------------------------------------------------------------------
# 使用家中wifi
# ------------------------------------------------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.zeczec.com/users/sign_in"
# url = "https://www.zeczec.com/"
driver = webdriver.Chrome()
driver.get(url)

email_blank = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("id", "user_email")))
email_blank.send_keys("nickmomo1524@gmail.com")
# time.sleep(30)

password_blank = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("id", "user_password")))
password_blank.send_keys("1aqzwx2s")
# time.sleep(30)

button = driver.find_element("name", "commit")
button.click()

print(1111111111)
import urllib.request as request
import bs4
new_url = "https://www.zeczec.com/"
req = request.Request(
    new_url, headers={'User-Agent': 'Mozilla/5.0'}#,'cookie':'over18=1'}
)

with request.urlopen(req) as response:
    webpage = bs4.BeautifulSoup(response.read().decode('utf-8'), features="html.parser")
blocks = webpage.find("button", class_="js-activatable-trigger")
print(blocks)

    # for block in blocks:
    #     sub_webpage_data_list=[]
    #     title = block.find("div", class_="title")
    #     number_count = block.find("div", class_="nrec")


# # time.sleep(60)
# personal_bar_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("type", "button")))
# # personal_bar_btn = driver.find_element("aria-label", "個人選單")
# personal_bar_btn.click()
# time.sleep(30)

# donated_record = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("href","/account")))
# # donated_record = driver.find_element("href","/account")
# donated_record.click()


# Wait for the checkbox to appear and click it
# check_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
# check_button.click()

time.sleep(30)
# ------------------------------------------------------------------------------------------------------------------------------
# 網頁暫放區域
# ------------------------------------------------------------------------------------------------------------------------------
# https://medium.com/marketingdatascience/selenium%E6%95%99%E5%AD%B8-%E4%B8%80-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8webdriver-send-keys-988816ce9bed
# https://medium.com/marketingdatascience/selenium%E6%95%99%E5%AD%B8-%E4%B8%80-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8webdriver-send-keys-988816ce9bed
# https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html

# 一些func 已經改動了
# https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el
# https://ithelp.ithome.com.tw/articles/10300961

# https://stackoverflow.com/questions/48365252/how-to-find-element-using-type-in-selenium-and-python

# 別人的半成品
# https://hackmd.io/@iampatrick/ryaJIdbX5

# 似乎是最佳解的方式
# https://www.zenrows.com/blog/selenium-stealth#conclusion
# https://app.zenrows.com/builder
# ------------------------------------------------------------------------------------------------------------------------------
# selenium 已經更新了，所以一些就無張的func 不會work
#         https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el

# ------------------------------------------------------------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium_stealth import stealth
# import random

# # create a new Service instance and specify path to Chromedriver executable
# service = ChromeService(executable_path=ChromeDriverManager().install())

# # Step 2: Change browser properties
# # create a ChromeOptions object
# options = webdriver.ChromeOptions()

# #run in headless mode
# options.add_argument("--headless")

# # disable the AutomationControlled feature of Blink rendering engine
# options.add_argument('--disable-blink-features=AutomationControlled')
 
# # disable pop-up blocking
# options.add_argument('--disable-popup-blocking')
 
# # start the browser window in maximized mode
# options.add_argument('--start-maximized')
 
# # disable extensions
# options.add_argument('--disable-extensions')
 
# # disable sandbox mode
# options.add_argument('--no-sandbox')
 
# # disable shared memory usage
# options.add_argument('--disable-dev-shm-usage')


# # Set navigator.webdriver to undefined
# # create a driver instance
# driver = webdriver.Chrome(service=service, options=options)

# # Change the property value of the navigator for webdriver to undefined
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")



# # Step 3: Rotate user agents 
# user_agents = [
#     # Add your list of user agents here
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
# ]

# # select random user agent
# user_agent = random.choice(user_agents)

# # pass in selected user agent as an argument
# options.add_argument(f'user-agent={user_agent}')


# # Step 4: Scrape using Stealth
# #enable stealth mode
# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )

# # navigate to opensea
# driver.get("https://opensea.io/")
 
# # Wait for page to load
# while driver.execute_script("return document.readyState") != "complete":
#     pass
 
# # Take screenshot
# driver.save_screenshot("opensea.png")
 
# # Close browser
# driver.quit()
