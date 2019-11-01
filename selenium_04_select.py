from selenium import webdriver
from selenium.webdriver.support.ui import Select
from array import *
import time, unittest

class SelectTest1 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("I:\Selenium\prac\web1.html")

    def test_multiple_selection(self):
        driver = self.driver

        # 리스트 개수 확인
        dropdown = Select(driver.find_element_by_name("cars"))
        self.assertEqual(4,len(dropdown.options))

        # 각각의 리스트 확인
        dropdown.select_by_visible_text("Volvo")
        self.assertEqual("Volvo",dropdown.first_selected_option.text)
        time.sleep(2)

        dropdown.select_by_value("saab")
        self.assertEqual("Saab",dropdown.first_selected_option.text)
        time.sleep(2)

        dropdown.select_by_index("2")
        self.assertEqual("Fiat",dropdown.first_selected_option.text)
        time.sleep(2)

        # 전체 리스트 확인
        exp_options = [ "Volvo", "Saab", "Fiat", "Audi"]
        act_options = []

        for option in dropdown.options:
            act_options.append(option.text)

        self.assertEqual(exp_options,act_options)
        print(act_options)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
