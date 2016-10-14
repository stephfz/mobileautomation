'''
@author: Dominik Dary
'''
import unittest
from selenium import webdriver


class FindElementTest(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {'aut': 'com.smarteragent.android.c21ace:5.400.01'}

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities
        )
        self.driver.implicitly_wait(30)

    def test_find_element_by_id(self):
        self.driver.get('com.smarteragent.android.AppLauncher')
        #self.assertTrue("and-activity://HomeScreenActivity" in self.driver.current_url)
        #my_text_field = self.driver.find_element_by_id('my_text_field')
        #my_text_field.send_keys('Hello Selendroid')

        #self.assertTrue('Hello Selendroid' in my_text_field.text)

    def tearDown(self):
        #self.driver.quit()
	print "quit"

if __name__ == '__main__':
    unittest.main()
