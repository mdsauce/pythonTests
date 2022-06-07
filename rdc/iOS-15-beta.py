# author Max Dobeck
from appium import webdriver
import os

desired_capabilities = {}
desired_capabilities['browserName'] = 'safari'
desired_capabilities['platformName'] = 'ios'
desired_capabilities['deviceName'] = 'iPhone .*'
desired_capabilities['name'] = 'CMDs are missing!'
desired_capabilities['newCommandTimeout'] = 10


username = os.getenv("SUPPORT_TEAM_ADMIN")
access_key = os.getenv("SUPPORT_TEAM_ADMIN_KEY")
credentials = f'https://{username}:{access_key}@'
US_ENDPOINT = credentials + 'ondemand.eu-central-1.saucelabs.com/wd/hub'

driver = webdriver.Remote(US_ENDPOINT, desired_capabilities)
try:
    print(driver.session_id)
    print(driver.desired_capabilities)
    driver.get('https://saucelabs.com')
    driver.get('https://bbc.co.uk')
    driver.get('https://status.saucelabs.com')
    # time.sleep(40)
    print("Device is up")
    # driver.quit()
except Exception as e:
    print("ERROR: ", driver.session_id, e)
