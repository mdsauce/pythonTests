from appium import webdriver
import traceback
from timeit import default_timer as timer
from datetime import timedelta
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')

desired_caps = {
    'safariLogAllCommunication': True,
    'deviceName': "iphone simulator",
    'platformName': "iOS",
    'browserName': "Safari",
    'platformVersion': "13.4",
    'appiumVersion': "1.17.1",
    'name': "ios safari test - emusim-3517",
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.us-west-1.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
try:
    start_pageload = timer()
    driver.get('http://alpha.realtor.com/realestateandhomes-search/Los-Angeles_CA?ab_vst=SWIPE_C&ads=0&tracking=0&split_tcv=157')
    end_pageload = timer()
    print(timedelta(seconds=end_pageload-start_pageload))
    # time.sleep(30)
    driver.quit()
except Exception:
    print(traceback.format_exc())
    print(driver.session_id)
    driver.quit()
