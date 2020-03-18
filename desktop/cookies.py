from selenium import webdriver
from sauceclient import SauceClient
from random import randint
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)
buildNum = randint(1, 1000)

desired_caps = {
    'platform': "Windows 10",
    'browserName': "internet explorer",
    'version': "latest",
    'name': "Cookie test",
    'build': "Cookies-%s" % buildNum
}

credentials = f'https://{username}:{access_key}@'
US_endpoint = credentials + 'ondemand.us-west-1.saucelabs.com/wd/hub'

try:
    driver = webdriver.Remote(
                            command_executor=US_endpoint,
                            desired_capabilities=desired_caps)
    # fetch all cookies from sites w/o cookies
    driver.get("https://news.ycombinator.com/")
    all_cookies = driver.get_cookies()

    # fetch all cookies from sites that do have cookies
    driver.get("https://saucelabs.com/")
    driver.add_cookie({'name': 'cookie_test', 'value': 'some_garbage_here'})
except Exception as e:
    print("Something went wrong:", e)
    sauce_client.jobs.update_job(driver.session_id, passed=False)

finally:
    sauce_client.jobs.update_job(driver.session_id, passed=True)
    driver.quit()
