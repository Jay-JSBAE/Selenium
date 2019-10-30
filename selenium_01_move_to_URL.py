import time
from selenium import webdriver

browser = webdriver.Chrome()

# ebay 페이지로 이동
browser.get("http://www.ebay.com")

# 검색창에 검색어를 입력하여 페이지 이동
searchbox = browser.find_element_by_id("gh-ac")
searchbox.send_keys("laptop")
searchbox.submit()
print("case01 success")
time.sleep(2)

# 링크 텍스트를 이용하여 페이지 이동
searchlink = browser.find_element_by_link_text("macbook")
searchlink.click()
print("case02 success")
time.sleep(2)

# elements를 이용하여 페이지 이동
choicelaptop = browser.find_element_by_xpath('//*[@id="srp-river-results-listing1"]/div/div[2]/a/h3')
choicelaptop.click()
print("case03 success")
time.sleep(2)

# webdriver 종료
browser.quit()
print('move to URL success')
