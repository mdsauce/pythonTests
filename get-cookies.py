from selenium import webdriver
from sauceclient import SauceClient
from random import randint
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)
buildNum = randint(1,1000)

desired_caps = {
    'platform': "Windows 10",
    'browserName': "internet explorer",
    'version': "latest",
    'name': "Cookie related test",
    'build':"Cookies-%s" % buildNum
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)

driver.get("https://news.ycombinator.com/")
all_cookies = driver.get_cookies()
print(all_cookies)

driver.get("about:blank")
all_cookies = driver.get_cookies()
print(all_cookies)


sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
