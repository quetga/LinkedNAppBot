from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = Service("/Users/jaquetwatkins/Desktop/Development/chromedriver\ 4")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")

time = driver.find_element(By.CSS_SELECTOR, '.event-widget time')
for t in time:
    print(t.text)

driver.quit()