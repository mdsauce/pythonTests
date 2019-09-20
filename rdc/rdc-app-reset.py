# author Max Dobeck
from appium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from appium.webdriver.common.touch_action import TouchAction
import time, os

desired_capabilities = {}
desired_capabilities['testobject_api_key'] = os.environ['CUSTOMER_APP']
desired_capabilities['platformName'] = 'android'
desired_capabilities['automationName'] = 'uiautomator2'
#desired_capabilities['appiumVersion'] = '1.10.0'
#desired_capabilities['platformVersion'] = '8' 
desired_capabilities['deviceName'] = ".*pixel*."

EU_endpoint = 'http://eu1.appium.testobject.com/wd/hub'
US_endpoint = 'http://us1.appium.testobject.com/wd/hub'

driver = webdriver.Remote(US_endpoint, desired_capabilities)
print(driver.session_id)
print(driver.desired_capabilities)

time.sleep(5)
print("I am going to reset the app now")
driver.reset()
time.sleep(10)
print("App is back up")

driver.quit()
