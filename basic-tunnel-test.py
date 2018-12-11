from selenium import webdriver
from sauceclient import SauceClient
from random import randint
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)
buildNum = randint(1,1000)

desired_caps = {
    'platform': "Windows 10",
    'browserName': "chrome",
    'version': "latest",
    'name': "Basic Test w a Build Number",
    'build':"My-hyphenated-test-%s" % buildNum,
    'tunnelIdentifier': "Test Me"
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
