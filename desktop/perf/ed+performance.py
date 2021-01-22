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
    'browserName': "chrome",
    'version': "latest",
    'sauce:options': {
        'extendedDebugging': True,
        'capturePerformance': True,
        'name': "ED + Perf capture",
        'commandTimeout': 250,
        'idleTimeout': 250,
    }
}
credentials = f'https://{username}:{access_key}@'
ENDPOINT = credentials + 'ondemand.us-west-1.saucelabs.com/wd/hub'

driver = webdriver.Remote(ENDPOINT, desired_capabilities=desired_caps)

try:
    driver.maximize_window()
    driver.get("https://saucelabs.com")
    driver.get("https://google.com")
    driver.get("https://speed.cloudflare.com")
except Exception as e:
    sauce_client.jobs.update_job(driver.session_id, passed=False)
    print(e)
    print(traceback.format_exc())
    print(driver.session_id)
    driver.quit()
    exit(1)

sauce_client.jobs.update_job(driver.session_id, passed=True)
driver.quit()
