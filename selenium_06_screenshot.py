from selenium import webdriver
#from array import *
import time, unittest

class screenshot (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("I:\Selenium\prac\web\select1_page.html")

    def test_screenshot(self):
        driver = self.driver
        driver.save_screenshot("I:\Selenium\prac\screenshot.png")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main()
