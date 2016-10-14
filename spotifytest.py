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
        desired_caps['deviceName'] = 'StephGalaxy'
        desired_caps['appPackage'] = 'com.smarteragent.android.c21'
	desired_caps['appPackage'] = 'com.spotify.music'
        desired_caps['appActivity'] = 'com.spotify.music.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
	#print "j"

    def test_add_contacts(self):
	time.sleep(10)
	'''
	#el = self.driver.find_element_by_accessibility_id("addressField")
	#el.send_keys("07024")
	textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("94301")
	el = self.driver.find_element_by_accessibility_id("com.smarteragent.android.c21:id/addressField")
	el.click()
	'''
	#el = self.driver.find_elements_by_class_name("android.widget.ImageButton")
	
#el = self.driver.find_element_by_accessibility_id("id/actionbar_item_create_playlist")
	el = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.spotify.music:id/action_bar_search")')
	el.send_keys("07024")
	#el[0].click()
 



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
