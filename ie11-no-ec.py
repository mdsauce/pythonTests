from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sauceclient import SauceClient
import os, sys

def teardown(quit_msg, exception):
  print("%s\n" % quit_msg, exception)
  print("%s" % driver.session_id)
  driver.quit()
  sys.exit(1)

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "windows 10",
    'browserName': "internet explorer",
    'version': "11.0",
    # 'seleniumVersion': "3.9.1",
    'name': "IE11 crash test - JWP no wait",
    #'tunnelIdentifier': "myTestTunnel"
}

try:
    driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
    driver.maximize_window()
    for i in range(150):
        driver.execute_script("sauce:context=Now moving to Google")
        driver.get("https://www.google.com")
        query_input = driver.find_element_by_name("q") 
        query_input.send_keys("This should NOT crash" + str(i))
    driver.execute_script("sauce:job-result=true")
except Exception as e:
    driver.execute_script("sauce:job-result=false")
    teardown("error on:\n", e)

driver.quit()
