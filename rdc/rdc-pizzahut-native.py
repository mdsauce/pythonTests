# Good example of how to start RDC Test
# Also example of dismissing/accepting an iOS alert
# author Max Dobeck
from appium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from appium.webdriver.common.touch_action import TouchAction
import time, os

desired_capabilities = {}
desired_capabilities['testobject_api_key'] = os.environ['PIZZASPECIAL'] 
desired_capabilities['platformName'] = 'ios'
desired_capabilities['appiumVersion'] = '1.9.1'
# 3. Where is your selected device located?
EU_endpoint = 'http://eu1.appium.testobject.com/wd/hub'
US_endpoint = 'http://us1.appium.testobject.com/wd/hub'

# The driver will take care of establishing the connection, so we must provide
# it with the correct endpoint and the requested capabilities.
driver = webdriver.Remote(US_endpoint, desired_capabilities)
time.sleep(4)
try: 
    alert = driver.switch_to_alert()
    alert.accept()
except NoAlertPresentException as e:
    print("No alert out there", e)
    pass

time.sleep(4)
driver.quit()
