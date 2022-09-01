import unittest
from appium import webdriver


class BasePage(unittest.TestCase):

    def setUp(self, true=None):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={"appium:automationName": "UiAutomator2",
                                  "appium:deviceName": "OnePlus 5T",
                                  "platformName": "Android",
                                  "appium:platformVersion": "10",
                                  "appium:noRest": "true",
                                  "appium:noReset": "true",
                                  "appium:skipUnlock": "false",
                                  "appium:app": "C:\\Users\\QUPS\\Downloads\\Viber.apk",
                                  "appium:autoGrantPermissions": 'true'

                                  }
        )
        print("Test Started.......")

    def tearDown(self):
        # self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
