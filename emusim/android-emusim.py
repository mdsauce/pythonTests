from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

caps = {}
caps['name'] = "Simple Android EMUSIM Test"
caps['appiumVersion'] = "1.15.0"
caps['deviceName'] = "Android GoogleAPI Emulator"
caps['deviceOrientation'] = "portrait"
caps['platformVersion'] = "8.1"
caps['platformName'] = "Android"
caps['browserName'] = "Chrome"


driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.\
com/wd/hub" % (username, access_key), desired_capabilities=caps)
driver.get("https://app.saucelabs.com")
sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
