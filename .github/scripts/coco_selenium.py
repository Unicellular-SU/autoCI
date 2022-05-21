import undetected_chromedriver as uc
from time import sleep
from subprocess import getoutput
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

# 获取chrome的主要版本号
version_str = getoutput('google-chrome --version')
#version_str="google chrome 100.0.13.77"
version_match = re.match( r'.*?(\d+).*', version_str)
global version_main
version_main = 99
try:
    version_main = int(version_match.group(1))
except:
    print("fail to get chrome version ")

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = uc.Chrome(options=options, version_main=version_main)

url = "https://www.cocomanga.com/js/custom.js"
driver.get(url)
sleep(10)
print(driver.page_source[0:200])

js = driver.find_element(by=By.CSS_SELECTOR, value="body").text
f = open("decrypted.js", "w")
f.write(js)
f.close()

driver.close()
driver.quit()
