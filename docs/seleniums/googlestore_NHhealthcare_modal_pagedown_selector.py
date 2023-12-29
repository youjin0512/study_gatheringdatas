# 구글플레이 - NH헬스케어

# 대상 : https://play.google.com/store/apps/details?id=com.nhlife.customer.healthcare&hl=ko-KR&pli=1

# 모달 화면 띄우기 : 평가 및 리뷰 클릭

# 댓글 모달 확인 : (css overflow:scroll or auto) div > div.fysCi

# 목적 : 댓글 마지막까지 스크롤 : scrollHeight 마지막인지 아닌지 확인(끝까지 스크롤 되면 종료됨)


# 댓글 개수 확인 : div.RHo1pe
# - scrollableDiv.scrollHeight                                  # 모달 현재 스크롤된 길이 확인
# - scrollableDiv.scrollTo(0, scrollableDiv.scrollHeight);      # 스크롤해서 아래로 내리기

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
browser.get("https://play.google.com/store/apps/details?id=com.nhlife.customer.healthcare&hl=ko-KR&pli=1")


from selenium.webdriver.common.by import By
# 모달 화면 띄우기 : 평가 및 리뷰 클릭
selector_element = "#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > header > div > div:nth-child(2) > button"
browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()


# - 정보 획득
# 댓글 모달 확인 : (css overflow:scroll or auto) div > div.fysCi
selector_element = "div.fysCi"        # fysCi : 댓글 가져오기
element_scrollableDiv = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)

# 스크롤 '전' 댓글 개수 확인 : div.RHo1pe
selector_element = 'div.RHo1pe'
elements_comment = browser.find_elements(by=By.CSS_SELECTOR, value=selector_element)
print("count comment before done scroll : {}".format(len(elements_comment)))

# 목적 : 댓글 마지막까지 스크롤 : scrollHeight 확인(마지막인지 아닌지 확인(끝까지 스크롤 되면 종료됨))
# 댓글 개수 확인 : div.RHo1pe
# - scrollableDiv.scrollHeight                                  # 모달 현재 스크롤된 길이 확인
# - scrollableDiv.scrollTo(0, scrollableDiv.scrollHeight);      # 스크롤해서 아래로 내리기(스크래핑)       # 현재 이 상태는 자바스크립트 언어라 파이썬 변수에 담아 사용해야함
previous_scrollHeight = 0
while True:
    # # python 방식 변수 매칭
    # print("{0}.scrollTo({1}, {0}.scrollHeight);"                        # 변수 재활용하여 포맷에 나열 : 인덱스 번호 부여
    #       .format(element_scrollableDiv, previous_scrollHeight,))
    # javascript와 python 결합 방식 변수 매칭
    browser.execute_script("arguments[0].scrollTo(arguments[1], arguments[0].scrollHeight);"  # scrollableDiv = 자바스크립트 arguments[0] = 파이썬 {0} 인덱스
                        ,element_scrollableDiv, previous_scrollHeight)  # arguments[1] = 0    # 키 다운해서

    # current_scrollHeight = browser.execute_script("return document.body.scrollHeight")      # 스크롤 확인
    current_scrollHeight = browser.execute_script("return arguments[0].scrollHeight"          # 위 주석처리한 내용과 동일한 내용임
                                                  ,element_scrollableDiv)                     # 스크롤 확인
    if previous_scrollHeight >= current_scrollHeight:
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass

# 스크롤 '후' 댓글 개수 확인 : div.RHo1pe
selector_element = 'div.RHo1pe'
elements_comment = browser.find_elements(by=By.CSS_SELECTOR, value=selector_element)
print("count comment after done scroll : {}".format(len(elements_comment)))

pass
# browser.save_screenshot('./formats_source.code_screenshotbyrun.png')


# 브라우저 종료
browser.quit()