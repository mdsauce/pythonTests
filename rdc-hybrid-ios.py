# Good example of how to start RDC Test
# Also example of dismissing/accepting an iOS alert
# author Max Dobeck
from appium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from appium.webdriver.common.touch_action import TouchAction
import time, os, sys

desired_capabilities = {}
desired_capabilities['testobject_api_key'] = os.environ['RDC_SALESFORCE_HYBRID']
desired_capabilities['platformName'] = 'iOS'
desired_capabilities['platformVersion'] = '12'
desired_capabilities['appiumVersion'] = '1.9.1'
desired_capabilities['name'] = 'Login To Sandbox'
# Where is your selected device located?
EU_endpoint = 'http://eu1.appium.testobject.com/wd/hub'
US_endpoint = 'http://us1.appium.testobject.com/wd/hub'

# The driver will take care of establishing the connection, so we must provide
# it with the correct endpoint and the requested capabilities.
driver = webdriver.Remote(US_endpoint, desired_capabilities)
time.sleep(4)

# accept the EULA
actions = TouchAction(driver)
eula_btn = driver.find_element_by_name('EULA.agree')
actions.tap(eula_btn)
actions.perform()

# wait for the load and then switch to sandbox
time.sleep(5)
env_btn = driver.find_element_by_name('login window gear')
actions.tap(env_btn)
actions.perform()
try:

    sandbox_btn = driver.find_element_by_name('Sandbox')
    actions.tap(sandbox_btn)
    actions.perform()
except Exception as e:
    print("Problem finding Sandbox button\n", e)
    driver.quit()
    sys.exit(1)

# login
try:
    time.sleep(8)
    user_text_box = driver.find_element_by_xpath('//XCUIElementTypeOther[@name="Login | Salesforce"]/XCUIElementTypeTextField')
    actions.tap(user_text_box)
    actions.perform()
    user_text_box.send_keys(os.environ['SFUSER'])
except Exception as e:
    print("Problem finding username textbox\n", e)
    driver.quit()
    sys.exit(1)

try:
    pass_text_box = driver.find_element_by_xpath('//XCUIElementTypeOther[@name="Login | Salesforce"]/XCUIElementTypeSecureTextField')
    actions.tap(pass_text_box)
    actions.perform()
    pass_text_box.send_keys(os.environ['SFPASS'])
except Exception as e:
    print("Problem finding user password textbox\n", e)
    driver.quit()
    sys.exit(1)

try:
    login_btn = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Log In to Sandbox"]')
    actions.tap(login_btn)
    actions.perform()
except Exception as e:
    print("Problem pressing the Login Button\n", e)
    driver.quit()
    sys.exit(1)

time.sleep(10)

try:
    allow_btn = driver.find_element_by_name('Allow')
    actions.tap(allow_btn)
    actions.perform()
except Exception as e:
    print("Problem pressing the Allow App Button\n", e)
    driver.quit()
    sys.exit(1)

# Allow the alert
try: 
    alert = driver.switch_to_alert()
    alert.accept()
except NoAlertPresentException as e:
    print("No alert out there", e)
    pass

time.sleep(10)

driver.quit()
print("The test passed!")
