from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

class Doubleclick (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///I:/Selenium/prac/web/04_doubleclick.html")

    def test_doubleclick(self):
        driver = self.driver
        text = driver.find_element_by_id("demo")

        ActionChains(self.driver).double_click(text).perform()
        self.assertEqual("rgba(255, 0, 0, 1)", text.value_of_css_property("color"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main()
