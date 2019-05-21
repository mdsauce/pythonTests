# auth: max dobeck
# written using python 3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from sauceclient import SauceClient
import os, time, datetime

username = os.environ['SAUCE_USERNAME']
access_key = os.environ['SAUCE_ACCESS_KEY']
sauce_client = SauceClient(username, access_key)

chrome_options = Options()
chrome_options.add_argument("--disable-web-security")

now = datetime.datetime.now()
build_name = "wait-siteload9-20s-reload-%d" % (now.day)
test_name = "wait-for-siteload-%d:%d:%d" % (now.hour, now.minute, now.microsecond)
desired_caps = {
    'platform': "macos 10.13",
    'browserName': "Chrome",
    'version': "69",
    'build': build_name,
    'name': test_name,
    'chromedriverVersion':"2.42"
}

try:
    driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps, options=chrome_options)

    wait = WebDriverWait(driver, 20)
    driver.set_page_load_timeout(90)
    driver.delete_all_cookies()
    driver.get("about:blank")
    driver.set_window_size(1080,1000)
    driver.get("https://secure01a.chase.com/web/auth")

    # wait for site to load
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "homepage")))
    except:
        driver.refresh()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "homepage")))

    # check that the site actually loaded and we're on the expected URL
    url = driver.current_url
    if url != "https://secure01a.chase.com/web/auth/#/logon/logon/chaseOnline":
        raise Exception("URL is not https://secure01a.chase.com/web/auth/#/logon/logon/chaseOnline")
    driver.add_cookie({'domain':'.chase.com','name':'adtoken.chase.com', 'value':'some-value', 'path':'/', 'httpOnly': False, 'secure': False})
    driver.add_cookie({'domain':'.chase.com', 'name':'X-Shape-Whitelist', 'value':'opt-in', 'path':'/', 'httpOnly': False, 'secure': False})
    driver.back()
    sauce_client.jobs.update_job(driver.session_id, passed=True)
except Exception as e:
    print("something went wrong!!")
    print(e, driver.session_id)
    sauce_client.jobs.update_job(driver.session_id, passed=False)
finally:
    driver.quit()
