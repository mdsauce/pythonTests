from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "windows 10",
    'browserName': "internet explorer",
    'version': "11.0",
    'seleniumVersion': "3.14.0",
    # 'seleniumVersion': "3.9.1",
    'name': "My basic IE11 test",
    #'tunnelIdentifier': "myTestTunnel"
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
