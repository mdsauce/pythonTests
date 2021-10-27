from selenium import webdriver
from sauceclient import SauceClient
import os


username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platformName': "Windows 10",
    'browserName': "chrome",
    'browserVersion': "latest",
    'goog:chromeOptions': {"args": ["--headless"]},
    'sauce:options':{
        "name":"Chrome Test", 
    }
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.us-west-1.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.get("https://www.google.com")

sauce_client.jobs.update_job(driver.session_id, passed=True)
print(driver.session_id)

driver.quit()
