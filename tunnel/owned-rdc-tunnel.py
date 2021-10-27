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
    'browserName': "",

    # 'name': "Testing if New tunnelOwner cap works w/ owned tunnel",
    # 'tunnelName': "my-tunnel"

    'name': "Testing if Old tunnelIdentifier cap works w/ owned tunnel",
    'tunnelIdentifier': "my-tunnel"
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.us-west-1.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.get("https://www.google.com")

driver.quit()