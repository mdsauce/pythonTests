# Ran using Python -version: 3.6.4.  Full Stack trace in the README.md
# This results in a VM running but timing out.  The VM will have the correct platform OS.  Stack trace error:
# selenium.common.exceptions.SessionNotCreatedException: Message: session not created exception: Missing or invalid capabilities
#   (Driver info: chromedriver=2.36.540470 (e522d04694c7ebea4ba8821272dbef4f9b818c91),platform=Windows NT 10.0.10586 x86_64)
# - Max Dobeck
from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platformName': "Windows 10",
    'browserName': "firefox",
    'browserVersion': "59",
    'sauce:seleniumVersion': "3.8.0"
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://www.google.com")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
