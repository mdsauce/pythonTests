# Ran using Python -version: 3.6.4.  Full Stack trace in the README.md
# This results in a VM session with the windows 2008 platform (reports as Windows 7).  The below stacktrace error is returned in the terminal:
# - Max Dobeck
from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platformName': "Windows 7",
    'browserName': "internet explorer",
    'browserVersion': "11", 
    'sauce:seleniumVersion': "3.9.1"
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.get("https://www.google.com")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
