# RDC on Sauce test using UP user
# Max Dobeck
from appium import webdriver
# from selenium.common.exceptions import NoAlertPresentException
# from appium.webdriver.common.touch_action import TouchAction
import os

device = "Samsung Galaxy S6.*"

desired_capabilities = {}
desired_capabilities['platformName'] = 'android'
desired_capabilities['privateDevicesOnly'] = True
desired_capabilities['platformVersion'] = 7
desired_capabilities['name'] = "Allocate Device " + device
desired_capabilities['deviceName'] = device
desired_capabilities['app'] = 'sauce-storage:app-release.apk'

username = os.environ['UP_USER']
userkey = os.environ['UP_USER_KEY']
credentials = f'https://{username}:{userkey}@'
US_endpoint = credentials + 'ondemand.us-west-1.saucelabs.com/wd/hub'

try:
    driver = webdriver.Remote(US_endpoint, desired_capabilities)
    print("\n\nTest", driver.capabilities['name'], "obtained device:",
          driver.capabilities['testobject_device_name'])
    print("Link to full Test here: ",
          driver.capabilities['testobject_test_report_url'])
    print("DeviceName Cap: ", device)
    print(driver.session_id)
except Exception as e:
    print("\nSomething went wrong >>>>>>>>>>>>>>>\n", e)
    exit(1)
driver.quit()
