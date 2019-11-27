from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sauceclient import SauceClient
import os, sys

def teardown(quit_msg, exception):
  print("%s\n" % quit_msg, exception)
  print("%s failed" % driver.session_id)
  driver.quit()
  sys.exit(1)

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)
us = 'https://ondemand.us-west-1.saucelabs.com/wd/hub'
eu = 'https://ondemand.eu-central-1.saucelabs.com/wd/hub'

desired_caps = {
    'platformName': 'windows 10',
    'browserName': 'internet explorer',
    'browserVersion': 'latest',
    'sauce:options': { 
        'name': "IE11 crash test - W3C wait",
        'username': username,
        'accessKey': access_key,
        # 'seleniumVersion': '3.11.0',
        # 'iedriverVersion': '3.12.0',
        # 'tunnelIdentifier': "myTestTunnel"
    }
}


try:
    driver = webdriver.Remote(command_executor=us, desired_capabilities=desired_caps)
    driver.maximize_window()
    wait = WebDriverWait(driver, 60)
    for i in range(150):
        driver.get("https://www.google.com")
        query_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        query_input.send_keys("This should NOT crash" + str(i))
    driver.execute_script("sauce:job-result=true")
except Exception as e:
    driver.execute_script("sauce:job-result=false")
    teardown("error on:\n", e)

driver.quit()
