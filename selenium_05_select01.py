from selenium import webdriver
from selenium.webdriver.support.ui import Select
from array import *
import time, unittest

class SelectTest1 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("I:\Selenium\prac\web\select1_page.html")

    def test_select(self):
        driver = self.driver

        # selection 태그에서 옵션의 개수 확인
        cars = Select(driver.find_element_by_name("multi_cars"))
        self.assertEqual(4, len(cars.options))

        # ctrl + click 효과 _ multiple choice
        cars.select_by_visible_text("Volvo")
        cars.select_by_value("multi_saab")
        cars.select_by_index(2)
        cars.select_by_index(3)
        time.sleep(2)
        # 선택 취소
        cars.deselect_by_visible_text("Volvo")
        cars.deselect_by_value("multi_saab")
        cars.deselect_by_index(2)
        cars.deselect_by_index(3)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
