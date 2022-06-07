# Good example of how to start RDC Test
# Max Dobeck

from appium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from appium.webdriver.common.touch_action import TouchAction
import time, os

# device = "iphone [78]||iphone xs||iphone x"
# device = "iPhone X.*|iPhone [78].*|iPad Pro 9.7|iPadAir21|iPadmini41|iPad Pro .*"
# device = "iPhone_11_13_real_us"
# device = "iPhone 13"
# device = "iphone 7|iphone 8"

desired_capabilities = {}
desired_capabilities['platformName'] = 'Android'
desired_capabilities['deviceName'] = '.*Pixel 6.*'
desired_capabilities['platformVersion'] = '12'
desired_capabilities['browserName'] = ''
desired_capabilities['privateDevicesOnly'] = 'true'
desired_capabilities['deviceOrientation'] = 'portrait'
desired_capabilities['name'] = "DeviceName Test using " + desired_capabilities['deviceName']

EU_endpoint = 'ondemand.eu-central-1.saucelabs.com/wd/hub'
US_endpoint = 'ondemand.us-west-1.saucelabs.com/wd/hub'
username = os.getenv("CUSTOMER_USER")
access_key = os.getenv("CUSTOMER_KEY")
credentials = f'https://{username}:{access_key}@'
ONDEMAND_ENDPOINT = credentials + EU_endpoint

try:
    driver = webdriver.Remote(ONDEMAND_ENDPOINT, desired_capabilities)
    print("\n\nTest", driver.capabilities['name'], " obtained device: ", driver.capabilities['testobject_device_name'])
    print("Link to full Test here: ", driver.capabilities['testobject_test_report_url'])
    # print("DeviceName Cap: ", device)
    # print(driver.session_id)
    # print(driver.desired_capabilities)
    driver.get("https://www.saucedemo.com/")
    # print(driver.page_source)
    time.sleep(6)
except Exception as e:
    print("Something went wrong >>>>>>>>>>>>>>>", e)
    exit(1)
# driver.quit()
