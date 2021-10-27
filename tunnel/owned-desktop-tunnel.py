# max dobeck
from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SUPPORT_SUB_ACCOUNT')
access_key = os.environ.get('SUPPORT_SUB_ACCOUNT_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "Windows 10",
    'browserName': "chrome",
    'version': "latest",
    # 'name': "Testing if New tunnelOwner cap works w/ owned tunnel",
    'name': "Testing if Old tunnelIdentifier cap works w/ owned tunnel",
    # 'build':"tunnel-cap-test",
    # 'tunnelName': "my-tunnel"
    'tunnelIdentifier': "my-tunnel"
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.us-west-1.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com")
driver.execute_script("sauce:context=Did that work?")

driver.quit()
