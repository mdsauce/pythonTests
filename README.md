# python tests

### Stack Trace from `selen-w3-python-test.py`
```python
Traceback (most recent call last):
  File "selen-w3-python-test.py", line 22, in <module>
    driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
  File "/Users/maxdobeck/.pyenv/versions/3.6.4/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py", line 154, in __init__
    self.start_session(desired_capabilities, browser_profile)
  File "/Users/maxdobeck/.pyenv/versions/3.6.4/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py", line 243, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "/Users/maxdobeck/.pyenv/versions/3.6.4/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "/Users/maxdobeck/.pyenv/versions/3.6.4/lib/python3.6/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: session not created exception: Missing or invalid capabilities
  (Driver info: chromedriver=2.36.540470 (e522d04694c7ebea4ba8821272dbef4f9b818c91),platform=Windows NT 10.0.10586 x86_64)
```

### Stack Trace from `selen-w3-sauce-prefix.py`
```python
Traceback (most recent call last):
  File "selen-w3-sauce-prefix.py", line 21, in <module>
    driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
  File "/Users/maxdobeck/.pyenv/versions/3.6.4/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py", line 154, in __init__
    self.start_session(desired_capabilities, browser_profile)
  File "/Users/maxdobeck/.pyenv/versions/3.6.4/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py", line 243, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "/Users/maxdobeck/.pyenv/versions/3.6.4/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "/Users/maxdobeck/.pyenv/versions/3.6.4/lib/python3.6/site-packages/selenium/webdriver/remote/errorhandler.py", line 208, in check_response
    raise exception_class(value)
selenium.common.exceptions.WebDriverException: Message: No browserName or device specified in session request. Please check our platforms documentation (https://saucelabs.com/docs/platforms): {'goog:chromeOptions': {'w3c': 'true'}, 'sauce:platform': 'Windows 10', 'sauce:browserVersion': '65', 'sauce:seleniumVersion': '3.8.0', 'sauce:browserName': 'chrome'}
```
