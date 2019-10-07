from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sauceclient import SauceClient
import os

def teardown(quit_msg, exception):
  print("%s\n" % quit_msg, exception)
  driver.quit()
  sys.exit(1)


username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "windows 10",
    'browserName': "chrome",
    'version': "beta",
    # 'build': "Static Build Name",
    'name': "Generic Chrome Latest Test",
    # 'tunnelIdentifier': "myTestTunnel"
    # 'goog:chromeOptions':{"w3c": "true"}
}

try:
  driver = webdriver.Remote(command_executor="http://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
  driver.maximize_window()
  driver.execute_script("sauce:context=Now moving to Google")
  driver.get("https://www.google.com")

  driver.get("https://saucelabs.com")
  wait = WebDriverWait(driver, 30)
  wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))

  driver.get("https://www.google.com/")
  query_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
  query_input.send_keys("Selenium Testing")
  driver.implicitly_wait(2)

  sauce_client.jobs.update_job(driver.session_id, passed=True)
except Exception as e:
  teardown("error:\n", e)



driver.quit()
