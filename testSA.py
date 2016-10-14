import os
import unittest
from appium import webdriver
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'StephGalaxy'
        desired_caps['appPackage'] = 'cl.tidchile.agrovva'
	desired_caps['appActivity'] = 'cl.tidchile.agrovva.activities.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
	#print "j"

    def test_add_contacts(self):
	time.sleep(15)


	#el = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.smarteragent.android.c21:id/addressField")')
	#el = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.smarteragent.android.c21:id/fName")')

	print el.text
	el.clear
	el.send_keys("98765")

	#el = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.smarteragent.android.c21:id/propImage")')
	#el.click()




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
