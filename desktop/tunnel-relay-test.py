from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from sauceclient import SauceClient
import os
import traceback

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "windows 10",
    'browserName': "firefox",
    'version': "latest",
}
credentials = f'http://{username}:{access_key}@'
ENDPOINT = credentials + 'localhost:4446/wd/hub'

driver = webdriver.Remote(ENDPOINT, desired_capabilities=desired_caps)

try:
    driver.maximize_window()

    driver.get("https://saucelabs.com")
    wait = WebDriverWait(driver, 60)
except Exception as e:
    sauce_client.jobs.update_job(driver.session_id, passed=False)
    print(e)
    print(traceback.format_exc())
    print(driver.session_id)
    driver.quit()
    exit(1)


sauce_client.jobs.update_job(driver.session_id, passed=True)
driver.quit()
