# Forcing a test to fail and declaring it a failure with the sauce_client

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from sauceclient import SauceClient
import os
import time

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
	'platform': "Windows 10",
    'browserName': "chrome",
    'version': "65.0"
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
time.sleep(5) # wait 5 seconds
driver.maximize_window()
driver.get("https://www.cnn.com")

if not "Google" in driver.title:
	sauce_client.jobs.update_job(driver.session_id, passed=False)
else:
	sauce_client.jobs.update_job(driver.session_id, passed=True)
driver.quit()
