# 2019.10.21
# Checkbox 처리

from selenium import webdriver
from array import *
import time, unittest

class CheckBoxTest (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_checkbox(self):
        driver = self.driver
        driver.get("I:\Selenium\prac\web1.html")
        car = driver.find_element_by_xpath("/html/body/form/input[2]")

        # 체크가 되어있지 않다면 체크
        if car.is_selected() == False:
            car.click()
        self.assertEqual(True,car.is_selected())

        # 체크 해제
        if car.is_selected():
            car.click()
        self.assertEqual(False,car.is_selected())
        print("check_test success!!!")

        # Element 검색 후 체크
        gender_type = driver.find_elements_by_name("gender")
        for type in gender_type:
            if type.get_attribute("value") == "male":
                type.click()
        print("find_elements success!!!")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
