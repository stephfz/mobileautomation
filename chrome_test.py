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
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'ephGalaxy'
	desired_caps['browserName'] = 'Chrome'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
	#print "j"

    def test_add_contacts(self):
	time.sleep(5)
	self.driver.get('google.com')
	#el = self.driver.find_elements_by_class_name("android.widget.EditText")
	#el.click()
	el[0].press_keycode("9")

 



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
