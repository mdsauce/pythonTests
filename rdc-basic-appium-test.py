# Good example of how to start RDC Test
# Also example of dismissing/accepting an iOS alert
# author Max Dobeck
from appium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from appium.webdriver.common.touch_action import TouchAction
import time, os

desired_capabilities = {}
desired_capabilities['testobject_api_key'] = os.environ['PIZZAPIZZA']
desired_capabilities['platformName'] = 'android'
desired_capabilities['automationName'] = 'uiautomator2'
desired_capabilities['appiumVersion'] = '1.10.0'
#desired_capabilities['platformVersion'] = '8' 
desired_capabilities['deviceName'] = ".*pixel*."
# 3. Where is your selected device located?
EU_endpoint = 'http://eu1.appium.testobject.com/wd/hub'
US_endpoint = 'http://us1.appium.testobject.com/wd/hub'

# The driver will take care of establishing the connection, so we must provide
# it with the correct endpoint and the requested capabilities.
driver = webdriver.Remote(US_endpoint, desired_capabilities)
print(driver.session_id)
print(driver.desired_capabilities)
time.sleep(4)
try: 
    alert = driver.switch_to_alert()
    alert.accept()
except NoAlertPresentException as e:
    print("No alert out there", e)
    pass

time.sleep(4)
driver.set_location(30.26, -97.74, 0)

actions = TouchAction(driver)
carryout_btn = driver.find_element_by_id('com.yum.pizzahut:id/carryoutButton')
actions.tap(carryout_btn)
actions.perform()

time.sleep(12)

driver.quit()
