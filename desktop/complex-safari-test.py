# Ran using Python -version: 3.6.4.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platformName': "mac 10.13",
    'browserName': "safari",
    'browserVersion': "12",
    'sauce:options': {
        'name': 'Complex test'
    }
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
query_input.send_keys(Keys.RETURN)
selenium_url = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Selenium Documentation")))
selenium_url.click()
textbook_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Test Design Considerations")))
textbook_link.click()

driver.get("https://www.google.com/")
query_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
query_input.send_keys("Selenium Testing")
query_input.send_keys(Keys.RETURN)
selenium_url = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Selenium Documentation")))
selenium_url.click()
textbook_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Test Design Considerations")))
textbook_link.click()

driver.get("https://www.google.com/")
query_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
query_input.send_keys("Selenium Testing")
query_input.send_keys(Keys.RETURN)
selenium_url = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Selenium Documentation")))
selenium_url.click()
textbook_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Test Design Considerations")))
textbook_link.click()

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()        
        
