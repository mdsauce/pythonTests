from selenium import webdriver
from sauceclient import SauceClient
import time
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
        'deviceName': "Android Emulator",
        'deviceOrientation': "landscape",
        'browserName': "Browser",
        'version': "latest",
        'platformVersion': "5.0",
        'platformName': "Android",
        'deviceType': "tablet",
        'name': "Android Tablet Test"
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.get("https://saucelabs.com")
sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
