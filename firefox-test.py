# Ran using Python -version: 3.6.4.  
from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "Windows 10",
    'browserName': "firefox",
    'version': "latest",
    'name': "Prefixtest: my_long_test_name_with_underscores_firefox_test_latest_browser_version_on_windows_10"
    #'tunnelIdentifier': "tunnelName"
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.get("https:/www.google.com")

if driver.current_url == "https://www.google.com/":
    sauce_client.jobs.update_job(driver.session_id, passed=True)
else: 
    sauce_client.jobs.update_job(driver.session_id, passed=False)

driver.quit()
