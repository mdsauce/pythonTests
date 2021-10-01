# author Max Dobeck
from appium import webdriver
import os

desired_capabilities = {}
desired_capabilities['browserName'] = 'safari'
desired_capabilities['platformName'] = 'ios'
desired_capabilities['platformVersion'] = '15'
desired_capabilities['deviceName'] = 'iPhone .*'
desired_capabilities['name'] = 'ios 15 beta RDC test'


username = os.getenv("SUPPORTTEAM_USER")
access_key = os.getenv("SUPPORTTEAM_KEY")
credentials = f'https://{username}:{access_key}@'
US_ENDPOINT = credentials + 'ondemand.eu-central-1.saucelabs.com/wd/hub'

driver = webdriver.Remote(US_ENDPOINT, desired_capabilities)
try:
    print(driver.session_id)
    print(driver.desired_capabilities)

    # time.sleep(10)
    print("Device is up")
    driver.quit()
except Exception as e:
    print("ERROR: ", driver.session_id, e)
