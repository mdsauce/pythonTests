from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from sauceclient import SauceClient
import os
import time
import traceback

username = os.getenv('SAUCE_USERNAME')
access_key = os.getenv('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "windows 10",
    'browserName': "chrome",
    'version': "latest",
    '_sauceCloudNode': os.getenv('SOBA', ''),
}
credentials = f'https://{username}:{access_key}@'
ENDPOINT = credentials + 'ondemand.us-west-1.saucelabs.com/wd/hub'

driver = webdriver.Remote(ENDPOINT, desired_capabilities=desired_caps)

try:
    print(driver.capabilities)
    driver.maximize_window()

    driver.get("https://saucelabs.com")
    wait = WebDriverWait(driver, 60)
    time.sleep(10)
except Exception as e:
    sauce_client.jobs.update_job(driver.session_id, passed=False)
    print(e)
    print(traceback.format_exc())
    print(driver.session_id)
    driver.quit()
    exit(1)


sauce_client.jobs.update_job(driver.session_id, passed=True)
driver.quit()
