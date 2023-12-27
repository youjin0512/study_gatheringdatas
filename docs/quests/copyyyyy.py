from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient
import time

# 웹드라이버 설정
webdriver_manager_directory = ChromeDriverManager().install()
# driver = webdriver.Chrome(ChromeDriverManager().install())
# Chrome WebDriver의 capabilities 속성 사용
# capabilities = browser.capabilities

# MongoDB 연결
def connect_mongo(collection_name):
    client = MongoClient("mongodb://localhost:27017/")
    database = client["gatheringdatas"]
    collection = database[collection_name]
    return collection
                                   
# 웹사이트 접속
webdriver.get("https://pedia.watcha.com/ko-KR/contents/mDWvXDd/comments")

# 웹사이트 스크롤링
def scroll_website():
    previous_scrollHeight = 0
    while True:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)
        current_scrollHeight = driver.execute_script("return document.body.scrollHeight")
        if previous_scrollHeight >= current_scrollHeight:
            break
        else:
            previous_scrollHeight = current_scrollHeight

scroll_website()

# 데이터 추출 및 DB 저장
def extract_data_and_save():
    collection = connect_mongo("watcha_comments")
    comment_elements = driver.find_elements(By.CSS_SELECTOR, 'div.css-1g3a7j2 > div.css-1bvtpon')

    for comment_element in comment_elements:
        try:
            writer = comment_element.find_element(By.CSS_SELECTOR, 'div.css-o6sgwe').text
            rate = comment_element.find_element(By.CSS_SELECTOR, 'span.css-1rwwus5').text
            contents = comment_element.find_element(By.CSS_SELECTOR, 'div.css-wnwcvo').text
            data = {'writer': writer, 'rate': rate, 'contents': contents}
            collection.insert_one(data)
        except Exception as e:
            print(f"Error occurred: {e}")

extract_data_and_save()

# 웹드라이버 종료
driver.quit()
