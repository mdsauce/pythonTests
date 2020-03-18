# Ran using Python -version: 3.6.4.
from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platformName': "macos 10.13",
    'browserName': "safari",
    'browserVersion': "12",
    'sauce:options': {
        'name': 'Safari 12 SE 3.14.0 --legacy tunnel test',
        'seleniumVersion': 'https://sauce-bundles.s3.amazonaws.com/selenium/selenium-server-3.14.0_safarilegacy.jar',
    }
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com")

sauce_client.jobs.update_job(driver.session_id, passed=True)
 
driver.quit()

