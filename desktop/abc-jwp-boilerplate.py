from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import traceback

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')

desired_caps = {
    'platform': "windows 10",
    'browserName': "firefox",
    'version': "latest",
    'build': "Flat Build",
}
credentials = f'https://{username}:{access_key}@'
ENDPOINT = credentials + 'ondemand.eu-central-1.saucelabs.com/wd/hub'

driver = webdriver.Remote(ENDPOINT, desired_capabilities=desired_caps)

try:
    driver.maximize_window()
    driver.get("https://saucelabs.com")
    wait = WebDriverWait(driver, 60)
except Exception as e:
    print(e)
    print(traceback.format_exc())
    print(driver.session_id)
    driver.quit()
    exit(1)

driver.quit()
