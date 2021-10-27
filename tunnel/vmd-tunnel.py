from appium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SUPPORT_SUB_ACCOUNT')
access_key = os.environ.get('SUPPORT_SUB_ACCOUNT_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    # 'deviceName': "iphone simulator",
    # 'browserName': "safari",
    # 'platformVersion': "13",
    # 'platformName': "iOS",

    'deviceName': "android emulator",
    'browserName': "chrome",
    'platformVersion': "8.0",
    'platformName': "android",

    'tunnelIdentifier': "deprecated-cap-test",
    'parentTunnel': "supportteam"

    # 'tunnelName': "deprecated-cap-test",
    # 'tunnelOwner': "supportteam"

    # 'tunnelName': "my-tunnel",
    # 'name': "VMD test New tunnelName cap",
        
    # 'name': "VMD test Old tunnelIdentifier cap",
    # 'tunnelIdentifier': "my-tunnel"
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.us-west-1.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
try:
    driver.get("https://saucelabs.com")
    sauce_client.jobs.update_job(driver.session_id, passed=True)
    driver.quit()
except Exception as e:
    print("something went wrong!!")
    print("Error: ", e, driver.session_id)
    sauce_client.jobs.update_job(driver.session_id, passed=False)
    driver.quit()
