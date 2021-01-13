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
    'platform': "Windows 10",
    'browserName': "Chrome",
    #'version': "latest",
    #'build': "Firefox Resolution Test",
    # 'name': "Gabeldy Gook Read a Book",
    #'screenResolution': "2560x1600"
    # 'tunnelIdentifier': "myTestTunnel"
    'goog:chromeOptions':{"w3c": "true"}
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com")

driver.get("https://saucelabs.com")
driver.get("https://www.google.com/")
driver.get("chrome://settings/help")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
