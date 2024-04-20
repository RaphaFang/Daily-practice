import urllib.request as request
import bs4
import json

url = "https://www.zeczec.com/"
req = request.Request(
    url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
)
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
# header 加上後面的作業系統，反而不讓進？

# # data = request.urlopen(req).read()
# with request.urlopen(req) as data:
#     data = json.load(data)

# with request.urlopen(req) as response:
#     webpage = bs4.BeautifulSoup(response.read().decode('utf-8'), features="html.parser")
# print(webpage)


from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
# driver_path = '/usr/local/bin/chromedriver'
# drvr = webdriver.Chrome(options = options, executable_path = driver_path)
# drvr.get('https://stackoverflow.com')


driver = webdriver.Chrome()
driver.get(url)
# data = request.urlopen(req).read()