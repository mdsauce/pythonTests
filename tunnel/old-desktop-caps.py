from selenium import webdriver
from sauceclient import SauceClient
# from random import randint
import os

username = os.environ.get('SUPPORT_SUB_ACCOUNT')
access_key = os.environ.get('SUPPORT_SUB_ACCOUNT_KEY')
sauce_client = SauceClient(username, access_key)
# build = randint(1,1000)

desired_caps = {
    'platform': "Windows 10",
    'browserName': "chrome",
    'version': "latest",
    'name': "Testing if old parentTunnel cap works",
    # 'build':"tunnel-cap-test%s" % build,
    'parentTunnel': "supportteam",
    'tunnelIdentifier': "deprecated-cap-test"
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.us-west-1.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com")
driver.execute_script("sauce:context=Did that work?")

driver.quit()
