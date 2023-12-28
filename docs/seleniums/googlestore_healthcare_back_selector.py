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
url = "https://play.google.com/store/search?q=%ED%97%AC%EC%8A%A4%EC%BC%80%EC%96%B4%EC%95%B1&c=apps&hl=ko-KR"
browser.get(url)

# - 정보 획득
from selenium.webdriver.common.by import By
# 앱 제조회사 리스트 : div > a.Si6A0c.Gy4nib
element_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a.Si6A0c.Gy4nib")

for company in element_companies :   # company : class
    company.click()
    time.sleep(1)   # 화면 완성 term
    # 앱 상세 제목 : div > h1
    element_title = browser.find_element(by=By.CSS_SELECTOR, value='div > h1')
    print("App comapny Name : {}".format(element_title.text))    #element_title : class
    
    browser.back()  # 제품 리스트로 이동(현재 브라우저 창에서 뒤로가기)
    time.sleep(1)   # 화면 완성 term
    pass
pass    

# 브라우저 종료
browser.quit()

# App comapny Name : Samsung Health(삼성 헬스)
# App comapny Name : NH헬스케어
# App comapny Name : 헬스케치-건강검진 기반 건강지표/위험도 분석,맞춤 헬스
# App comapny Name : 케어헬스
# App comapny Name : 헬스 커넥트(베타)
# App comapny Name : 헬스케어 건강관리서비스
# App comapny Name : 케어센스 에어
# App comapny Name : 오케어
# App comapny Name : CAZZLE (캐즐)
# App comapny Name : 어떠케어 - 내 몸이 궁금할 때
# App comapny Name : 헬스퀘어
# App comapny Name : 헬스월릿(HealthWallet) -건강을 월릿하다!
# App comapny Name : Health&u 헬스앤유
# App comapny Name : 애니핏 플러스 나에게 핏한 건강관리
# App comapny Name : 하티브케어 - 심전도, 혈압, 혈당 등 기록 관리 앱
# App comapny Name : 현대해상 하이헬스챌린지
# App comapny Name : 헬스 데이터뱅크
# App comapny Name : Health4U
# App comapny Name : 헬퍼 - 간병일자리 찾기, 일자리 알림 받기, 간병인
# App comapny Name : 해피민트 - 직장인 멘탈헬스케어 앱
# App comapny Name : 하나손해보험헬스케어
# App comapny Name : 올라케어 - 건강한 일상의 시작
# App comapny Name : 케어네이션 - 간병인, 병원 동행인, 요양보호사 찾기
# App comapny Name : Health Keeper