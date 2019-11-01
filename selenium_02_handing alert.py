# 2019.08.30
# Alert 처리

import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///H:/Selenium/prac/alert.html")
time.sleep(2)

# simpleAlert 버튼 클릭
first_button = driver.find_element_by_id("simpleAlert")
first_button.click()
time.sleep(2)
# Alert 창의 메시지 확인 후 확인 버튼
alert1 = driver.switch_to.alert
message = alert1.text
print("Alert1 message : " + message)
alert1.accept()
print("first_button success!!!")
time.sleep(2)

# 두번째 버튼 클릭
second_button = driver.find_element_by_id("confirmAlert")
second_button.click()
time.sleep(2)

# 확인 버튼 클릭
alert2 = driver.switch_to.alert
alert2.accept()
time.sleep(1)
second_button.click()
time.sleep(1)
# 취소 버튼 클릭
alert2.dismiss()
time.sleep(2)
print("second_button success!!!")

# 세번째 버튼 클릭
third_button = driver.find_element_by_id("promptAlert")
third_button.click()
time.sleep(2)

# alert 텍스트 입력
alert3 = driver.switch_to.alert
alert3.send_keys("Jay.Bae")
time.sleep(2)
# 확인 버튼 클릭
alert3.accept()
message3 = driver.find_element_by_id("promptMemo")
print("Alert3 Message : " + message3.text)
print("third_button success!!")
time.sleep(2)

# webdriver 종료
driver.quit()
print("Alert_test success!!!!")
