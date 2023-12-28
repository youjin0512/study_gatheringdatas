# * 웹 크롤링 동작      # 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://getbootstrap.com/docs/5.3/examples/checkout/")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
# refer official : https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select
from selenium.webdriver.support.ui import Select
# Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)  # driver.find_element(By.TAG_NAME, “select” : select에 있는 element(tag)

# 국가 selectbox 선택 
selector_element = '#country'
element_country = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
Select(element_country).select_by_index(1)  # index(1) : 리스트 중 2번째 항목
# 주 selectbox 선택 
selector_element = '#state'
element_state = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
Select(element_state).select_by_index(1)   # index(1) : 리스트 중 2번째 항목

# browser.save_screenshot('./formats_source.code_screenshotbyrun.png')
pass

# 브라우저 종료
browser.quit()