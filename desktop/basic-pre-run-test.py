# Basic test with pre-run executable
from selenium import webdriver
from sauceclient import SauceClient
import time
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "windows 7",
    'browserName': "internet explorer",
    'version': "11.0",
    'name': "My Windows Bgrd PreRun.exe Test",
    'prerun': {
        # 'executable': 'sauce-storage:BrowserAuthenticationAdv.exe',
        # 'executable': 'https://gist.github.com/DylanLacey/f3f03296718783f52e4938d7845d3660',
        'executable': "https://gist.githubusercontent.com/bertinwong-saucelabs/8a38ed0371eec5dfefa576c917beac18/raw/b17cfb54aab0f14106473091b922415ea90ef4c0/refresh_wininet.bat",
        'background': 'true',
        # 'args': [ '--silent', '-a', '-q' ]
    }
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
time.sleep(3)
driver.maximize_window()
driver.get("https://saucelabs.com")

driver.quit()
