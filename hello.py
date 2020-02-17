# -*- coding: utf-8 -*-
from appium import webdriver
import time

def desired_capabilities(language, locale):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '9',
        'deviceName': '98899546314a554649',
        'app': '/Users/admin/Downloads/testautomationfleetapp/apk/fms-release-4.34.2.1923.apk',
        'appPackage': 'se.scania.fms' ,
        'language': str(language),
        'locale': str(locale),
        'adbExecTimeout': '10000000'


    }
    return desired_caps

class LoginTest():

    def setUp(self):
        english_setup = desired_capabilities('en', 'EN')
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', english_setup)

    def tearDown(self):
        time.sleep(4)
        self.driver.quit()
        time.sleep(4)


    def test_1_login_with_username(self):

        self.setUp()
      
        self.driver.find_element_by_id('se.scania.fms:id/userName').send_keys("hello")




logintest = LoginTest()
logintest.test_1_login_with_username()


