# Basic test with an optional w3c capability for chrome
from selenium import webdriver
from sauceclient import SauceClient
from selenium.webdriver.common.keys import Keys
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "Windows 10",
    'browserName': "chrome",
    'version': "latest",
    # 'seleniumVersion': "3.9.1",
    'name': "Chrome ExtendedDebugging Response Test",
    'extendedDebugging': "true"
    # 'tunnelIdentifier': "RandomWords"
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.implicitly_wait(30)
driver.maximize_window()
driver.execute_script("sauce:context=Now GETting google.com")
driver.get("https://www.google.com")
searchBar = driver.find_element_by_name("q")
searchBar.send_keys('npr', Keys.ENTER)

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
