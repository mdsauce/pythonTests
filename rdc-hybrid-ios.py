# Good example of how to start RDC Test
# Also example of dismissing/accepting an iOS alert
# author Max Dobeck
from appium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from appium.webdriver.common.touch_action import TouchAction
import time, os, sys

def context_check(page="none"):
    if page != "none":
        print("We are at the %s page" % page)
    contexts = driver.contexts
    print("%d contexts" % (len(contexts)))
    print("All Contexts: ", driver.contexts)
    print("Current Context is ", driver.current_context, "\n")
    

desired_capabilities = {}
desired_capabilities['testobject_api_key'] = os.environ['RDC_SALESFORCE_HYBRID']
desired_capabilities['platformName'] = 'iOS'
desired_capabilities['platformVersion'] = '12'
desired_capabilities['appiumVersion'] = '1.9.1'
desired_capabilities['name'] = 'Assert Context or Contexts CMDs Do Not Timeout'
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
context_check("Login")
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

time.sleep(8)

# Accept app stuff
context_check("Allow App Permissions")
try:
    #allow_btn = driver.find_element_by_accessibility_id(' Allow ')
    allow_btn = driver.find_element_by_xpath('//XCUIElementTypeButton[@name=" Allow "]')
    actions.tap(allow_btn)
    actions.perform()
except Exception as e:
    print("Problem pressing the Allow App Button.  Switching contexts\n", e)
    driver.switch_to.context(driver.contexts[1]) # Loop here over all contexts.  Maybe make a fn
    context_check()
    allow_btn = driver.find_element_by_xpath('//XCUIElementTypeButton[@name=" Allow "]')
    actions.tap(allow_btn)
    actions.perform()
except Exception as e:
    print("Could not press the Allow App Button\n", e)
    driver.quit()
    sys.exit(1)

# Allow the OS alert
try:
    time.sleep(4)
    driver.switch_to.context('NATIVE_APP')
    context_check("Allow OS Popup")
    alert = driver.switch_to.alert
    alert.accept()
except Exception as e:
    print("Could not press the Allow App Button\n", e)
    print(driver.page_source)
    driver.quit()
    sys.exit(1)

time.sleep(10)

context_check()

directory = '%s/' % os.getcwd()
file_name = 'last-part-of-rdc-hybrid-ios-test.png'
driver.save_screenshot(directory + file_name)

driver.quit()
print("The test passed!")
