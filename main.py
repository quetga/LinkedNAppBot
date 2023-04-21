import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

myemail = "your-email"
mypassword = "your-password"
PHONE = "your-phone-number"

chrome_driver_path = Service('/Users/jaquetwatkins/Desktop/Development/chromedriver 4')
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3529145608&distance=25&f_AL=true&geoId=90000052&keywords=it%20support&location=Atlanta%20Metropolitan%20Area&refresh=true")

#auto sign-in
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(myemail)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(mypassword)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title")

for listing in all_listings:
    print("called")

    listing.click()
    time.sleep(5)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_button.click()
        time.sleep(5)

        submit_button = driver.find_element(By.LINK_TEXT, "Submit application")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("LINK_TEXT") == "ember507":
            close_button = driver.find_element(By.CLASS_NAME, "mercado-match")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue
time.sleep(5)
driver.quit()