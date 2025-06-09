from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://divar.ir/s/tehran/service-jobs?q=%D8%AA%D9%88%D8%A7%D9%81%D9%82%DB%8C")  # آدرس دقیق رو بذار
all_ads_text = []


last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    ads = driver.find_elements(By.CSS_SELECTOR, "div.widget-col-d2306")
    for ad in ads:
            all_ads_text.append(ad.text)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



matching_ads = []

for ad in all_ads_text:
    if "پرداخت توافقی" in ad:
        matching_ads.append(ad)
        print("found: \n", ad)


print("all matches:", len(matching_ads))

