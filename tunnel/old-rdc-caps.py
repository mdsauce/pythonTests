from selenium import webdriver
from sauceclient import SauceClient
# from random import randint
import os

username = os.environ.get('SUPPORT_SUB_ACCOUNT')
access_key = os.environ.get('SUPPORT_SUB_ACCOUNT_KEY')
sauce_client = SauceClient(username, access_key)
# build = randint(1,1000)

desired_caps = {
    'platformName': "iOS",
    'deviceName': "iphone .*",
    'platformVersion': "14",
    'name': "Testing if Old parentTunnel caps works on RDC",
    'browserName': "",
    # 'build':"tunnel-cap-test%s" % build,
    'parentTunnel': "supportteam",
    'tunnelIdentifier': "deprecated-cap-test"
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.us-west-1.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.get("https://www.google.com")

driver.quit()