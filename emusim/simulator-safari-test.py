from appium import webdriver
from sauceclient import SauceClient
import time
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'deviceName': "iphone simulator",
    'browserName': "safari",
    'platformVersion': "13",
    'platformName': "iOS",
    'tunnelName': "my-tunnel"
    # 'tunnelIdentifier': "my-tunnel"
    # 'name': "iOS Sim Test Window Maximize",
    
    # 'Build': "maximize current window bug"
    # 'deviceName': "android emulator",
    # 'browserName': "chrome",
    # 'platformVersion': "8.0",
    # 'platformName': "android",
    # 'appiumVersion': "1.9.1",
    # 'name': "android emu Test Window Maximize",
}

try:
    driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.us-west-1.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)

    # driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    ctx = driver.context
    print("current context: ", ctx)
    driver.get("https://saucelabs.com")
    sauce_client.jobs.update_job(driver.session_id, passed=True)
    driver.quit()
except Exception as e:
    print("something went wrong!!")
    print("Error: ", e, driver.session_id)
    sauce_client.jobs.update_job(driver.session_id, passed=False)
    driver.quit()
