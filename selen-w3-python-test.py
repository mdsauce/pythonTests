from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
	'sauce:platformName': "Windows 10",
    'sauce:browserName': "chrome",
    'sauce:browserVersion': "65",
    'sauce:seleniumVersion': "3.8.0"
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://www.google.com")

if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
    sauce_client.jobs.update_job(driver.session_id, passed=False)
else
	sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
