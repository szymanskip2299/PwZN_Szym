from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name",type = str)
args = parser.parse_args()
file_name=args.file_name


options = Options()

options.add_argument('--disable-notifications')

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service = service, options = options)

driver.get('https://www.visiticeland.com/')
print("asas")
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
 'body > section > div.ch2-container.ch2-theme-bar.ch2-style-light.ch2-ea.ch2-block > div.ch2-dialog.ch2-dialog-bottom.ch2-visible > div.ch2-dialog-actions.ch2-dialog-actions-vertical > div:nth-child(2) > button')))
print("asas")
button.click()
print("asas")

# plan_your_trip = driver.find_element(By.CSS_SELECTOR,"#main-content > nav > div > div > div.w-100.justify-content-center.d-none.d-lg-flex > div:nth-child(2) > button")
# plan_your_trip.
plan_your_trip =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#main-content > nav > div > div > div.w-100.justify-content-center.d-none.d-lg-flex > div:nth-child(2) > button")))
plan_your_trip.click()
things_to_do = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#main-content > nav > div > div > div.w-100.justify-content-center.d-none.d-lg-flex > div:nth-child(2) > div > a:nth-child(3)")))
time.sleep(0.5)
things_to_do.click()
culture = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#main-content > div.page-wrap > article > div > div.d-flex > div.things-to-do__mobile__filters--closed > div > div:nth-child(1) > div > button:nth-child(2) > label")))
culture.click()


# 
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# time.sleep(1)
# for _ in range(4):
#     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)

table = driver.find_element(By.CSS_SELECTOR, "#main-content > div.page-wrap > article > div > div.d-flex > div.w-100 > div.search-result-grid.p-0.pl-0")


to_json=[]
for element in table.find_elements(By.CLASS_NAME,'react-reveal'):
    title=element.find_element(By.CLASS_NAME,"pt-2").text
    desc=element.find_element(By.CLASS_NAME,"search-result-grid__card__text__description").text
    href=element.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
    print(title+"\t\t"+desc+"\t\t"+href)
    to_json.append([title,desc,href])


with open(file_name, 'w') as f:
    json.dump(to_json, f)


time.sleep(1000)

driver.close()

# poetry run python .\proj5.py "test.json"