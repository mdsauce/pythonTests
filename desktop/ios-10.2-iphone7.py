from selenium import webdriver
from sauceclient import SauceClient
import time
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

caps = {}
caps['browserName'] = "Safari"
caps['deviceName'] = "iPhone 7 Simulator"
caps['deviceOrientation'] = "portrait"
caps['platformVersion'] = "10.2"
caps['platformName'] = "iOS"

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=caps)
driver.get("https://saucelabs.com")
sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
