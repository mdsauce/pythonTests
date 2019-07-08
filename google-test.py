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
    'platform': "macOS 10.12",
    'browserName': "chrome",
    'version': "61",
    'build': "Chrome Mac Google Test",
    'name': "testGoogle",
    'tunnelIdentifier': "myTestTunnel"
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
sauce_client.jobs.update_job(driver.session_id, passed=False)

driver.maximize_window()
driver.get("https://www.google.com")
title = driver.title
print(title)
wait = WebDriverWait(driver, 60)
query_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
query_input.send_keys("Intuit")
title = driver.title
print(title)

sauce_client.jobs.update_job(driver.session_id, passed=True)
driver.quit()
