from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sauceclient import SauceClient
import os


# username = os.environ.get('SAUCE_USERNAME')
# access_key = os.environ.get('SAUCE_ACCESS_KEY')
username = 'RAishwarya'
access_key = '880a7cf0-f887-4494-858a-f49034ca3818'
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "macos 10.13",
    'browserName': "safari",
    'version': "11.1",
    'build': "Static Build Name",
    'name': "Reused Generic Test Name",
    # 'tunnelIdentifier': "myTestTunnel"
    # 'goog:chromeOptions':{"w3c": "true"}
}

driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.execute_script("sauce:context=Now moving to Google")
driver.get("https://www.google.com")

driver.get("https://saucelabs.com")
wait = WebDriverWait(driver, 60)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "site-container")))
if driver.title != "Cross Browser Testing, Selenium Testing, and Mobile Testing | Sauce Labs":
    sauce_client.jobs.update_job(driver.session_id, passed=False)
    driver.quit()

driver.get("https://www.google.com/")
query_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
query_input.send_keys("Selenium Testing")
search = wait.until(EC.presence_of_element_located((By.NAME, "btnK")))
search.click()
driver.implicitly_wait(2)

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
