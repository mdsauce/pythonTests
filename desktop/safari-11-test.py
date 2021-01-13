from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sauceclient import SauceClient
import os


username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "macos 10.13",
    'browserName': "safari",
    'version': "11.1",
    'name': "safari11 assert this passes",
    'username': username,
    'access_key': access_key,
    # 'seleniumVersion':"3.14.0_safarilegacy",
    # 'tunnelIdentifier': "myTestTunnel"
}

driver = webdriver.Remote(command_executor="http://ondemand.saucelabs.com/wd/hub", desired_capabilities=desired_caps)
driver.maximize_window()
driver.get("https://saucelabs.com")

driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com/")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
