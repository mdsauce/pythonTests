from appium import webdriver

desired_capabilities = {}
desired_capabilities['testobject_api_key'] = 'C00524B2951A4FE588E7D234E663BC0D'
desired_capabilities['platformName'] = 'Android'
desired_capabilities['platformVersion'] = '8' 
# 3. Where is your selected device located?
EU_endpoint = 'http://eu1.appium.testobject.com/wd/hub'
US_endpoint = 'http://us1.appium.testobject.com/wd/hub'

# The driver will take care of establishing the connection, so we must provide
# it with the correct endpoint and the requested capabilities.
driver = webdriver.Remote(US_endpoint, desired_capabilities)

driver.quit()