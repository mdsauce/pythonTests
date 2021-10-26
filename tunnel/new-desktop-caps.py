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
    'name': "Testing if new tunnelOwner cap works",
    'build':"tunnel-cap-test",
    'tunnelOwner': "supportteam",
    'tunnelName': "deprecated-cap-test"
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.us-west-1.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com")
driver.execute_script("sauce:context=Did that work?")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
