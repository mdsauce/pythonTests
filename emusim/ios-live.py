from selenium import webdriver
import time
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')

desired_caps = {
    'deviceName': "iphone simulator",
    'platformName': "iOS",
    'browserName': "",
    'platformVersion': "12.0",
    'name': 'ios live test',
    'app': "sauce-storage:walmart-prod.zip",
}

try:
    driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
    time.sleep(30)
    driver.quit()
except Exception as e:
    print(e)
