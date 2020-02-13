from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sauceclient import SauceClient
import os


username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "windows 10",
    'browserName': "firefox",
    'version': "latest",
    'build': "Static Build Name",
    'name': "This job should be public",
    'public': "public"
    # 'tunnelIdentifier': "myTestTunnel"
    # 'goog:chromeOptions':{"w3c": "true"}
}
credentials = f'https://{username}:{access_key}@'
US_endpoint = credentials + 'ondemand.us-west-1.saucelabs.com/wd/hub'

driver = webdriver.Remote(US_endpoint, desired_capabilities=desired_caps)
driver.maximize_window()
driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com")

driver.get("https://saucelabs.com")
wait = WebDriverWait(driver, 60)
if driver.title != "Cross Browser Testing, Selenium Testing,\
and Mobile Testing | Sauce Labs":
    sauce_client.jobs.update_job(driver.session_id, passed=False)
    driver.quit()

driver.get("https://www.google.com/")
query_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
query_input.send_keys("Selenium Testing")
search = wait.until(EC.presence_of_element_located((By.NAME, "btnK")))
search.click()
driver.implicitly_wait(2)

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
