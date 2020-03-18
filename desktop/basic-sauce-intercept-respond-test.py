from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "Windows 10",
    'browserName': "chrome",
    'version': "latest",
    'name': "Sauce Intercept and Respond Test",
    'tunnelIdentifier': "fakeBusiness",
    'extendedDebugging': "true"
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.implicitly_wait(8)
driver.execute_script("sauce:context=Now going to localhost")
driver.get("http://127.0.0.1:3000/")
apiButton = driver.find_element_by_id('apiTest')
apiButton.click()

driver.execute_script("sauce:intercept", {
    "url": 'http://api.fakeurl.com/v1/test',
    "respond": {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "rawResponse": "{\"TestString\":\"OK\"}"
    }
})

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
