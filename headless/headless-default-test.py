import os
import sys
import new
import unittest
from selenium import webdriver
USERNAME = os.environ.get('SAUCE_USERNAME')
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
HOST = os.environ.get('HOST', 'ondemand.us-east1.saucelabs.com')
SAUCE_HOST = '.'.join(HOST.split('.')[1:])
PORT = os.environ.get('PORT', 443)
SCHEME = os.environ.get('SCHEME', 'https')
browsers =  [{"platform": "Linux",
              "browserName": "chrome",
              "version": "71"},
             {"platform": "Linux",
              "browserName": "chrome",
              "version": "72"},
             {"platform": "Linux",
              "browserName": "chrome",
              "version": "73"},
             {"platform": "Linux",
              "browserName": "firefox",
              "version": "62"},
             {"platform": "Linux",
              "browserName": "firefox",
              "version": "63"},
             {"platform": "Linux",
              "browserName": "firefox",
              "version": "64"}]
 
def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator
 
@on_platforms(browsers)
class SauceSampleTest(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        sauce_url = "%s://%s:%s@%s:%s/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (SCHEME, USERNAME, ACCESS_KEY, HOST, PORT)
        )
    def test_sauce(self):
        self.driver.get('http://saucelabs.com/test/guinea-pig')
        assert "I am a page title - Sauce Labs" in self.driver.title
        comments = self.driver.find_element_by_id('comments')
        comments.send_keys('Hello! I am some example comments.'
                           ' I should be in the page after submitting the form')
        self.driver.find_element_by_id('submit').click()
        commented = self.driver.find_element_by_id('your_comments')
        assert ('Your comments: Hello! I am some example comments.'
                ' I should be in the page after submitting the form'
                in commented.text)
        body = self.driver.find_element_by_xpath('//body')
        assert 'I am some other page content' not in body.text
        self.driver.find_elements_by_link_text('i am a link')[0].click()
        body = self.driver.find_element_by_xpath('//body')
        assert 'I am some other page content' in body.text
    def tearDown(self):
        print("Link to your job: https://%s/jobs/%s" %
              (SAUCE_HOST, self.driver.session_id))
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main()