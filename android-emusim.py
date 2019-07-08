from selenium import webdriver
from sauceclient import SauceClient
import time
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

caps = {}
caps['deviceName'] = "Android Emulator"
caps['browserName'] = "Chrome"
caps['platformName'] = "Android"
caps['platformVersion'] = "8.0"
caps['androidVersion'] = "1.11.1"


driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=caps)
driver.get("https://app.saucelabs.com")
sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
