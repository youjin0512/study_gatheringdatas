# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000213114")  # 해석 : 브라우저 안에서 이 url, element를 가져온다

# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div.mnemitem_unit"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)   # value : 전체(#ty_thmb_view > ul > li:nth-child(2) > div)

for element_item in element_bundle[10:41] :     # element_bundle : list[webelement] / [] : 슬라이스해서 인덱스 사용 -> 보고 싶은곳만 확인 => 'list slicing'
    # print(element_item.text)   # element_item = webelement = 'class'    # 상품 정보들 (전체) 프린트
    #상품 제목(title)
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value="span.mnemitem_goods_tit")    # value = 타이틀 / 변수로 담아서 str으로 넣으면 좋음
    title = element_title.text
    # print("title : {}".format(title))
    # 상품 판매 원가(old price) (try~except 포함)
    try :   
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value="div > del > em")    # div > del > em : element 접근자
        old_price = element_old_price.text    # old_price : 이 부분에 값이 있거나 공란으로 들어가야함 (공란인 이유? : old price가 없는 경우 있어서)
        pass    # 정식 코드
    except :
        old_price = ""     # 특정 항목에서는 태그가 없을 수 있다
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass    # try나 except이 끝난 후 무조건 실행 코드

    print("title : {}, old price : {}".format(title, old_price))
   
    pass
pass

# 브라우저 종료
browser.quit()


## title만 프린트 했을 했을 떄 
# 정상가격
# 19,900 원
# 할인율
# 10%
# 판매가격
# 17,900
# 원
# 100g 당 1,194원
# 상품평점 5점 만점에
# 4.4
# 상품평 개수
# (2,503)
# 신선보장
# 장바구니 담기
# 쓱배송
# 완숙토마토 5~8입/팩 (1.1kg)
# 정상가격
# 13,800 원
# 할인율
# 21%
# 판매가격
# 10,800
# 원
# 100g 당 982원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (31,440)
# 신선보장
# #간식 #쥬스용
# 장바구니 담기
# 쓱배송
# [칠레산] 생블루베리 310g/팩
# 정상가격
# 12,580 원
# 할인율
# 39%
# 판매가격
# 7,580
# 원
# 100g 당 2,446원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (22,440)
# 신선보장
# #건강간식 #새콤달콤
# 장바구니 담기
# 쓱배송
# 대추방울토마토 1kg/팩
# 판매가격
# 10,980
# 원
# 100g 당 1,098원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (41,821)
# 신선보장
# #대추방울토마토 #방울토마토
# 장바구니 담기
# 쓱배송
# 신세계푸드 [에콰도르산] 하루과일 바나나/팩 (420g내외)
# 판매가격
# 1,980
# 원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (16,053)
# 신선보장
# 장바구니 담기
# 쓱배송
# 스미후루 [필리핀산] 고당도 감숙왕 바나나 (1.2kg내외)
# 판매가격
# 3,980
# 원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (9,994)
# 신선보장
# 장바구니 담기
# 쓱배송
# 더달콤 스테비아 대추방울토마토 550g/팩
# 정상가격
# 9,980 원
# 할인율
# 20%
# 판매가격
# 7,980
# 원
# 100g 당 1,451원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (21,938)
# 신선보장
# #방울토마토
# 장바구니 담기
# 쓱배송
# 파머스픽 당도선별사과 1.2kg/봉 (5~6입)
# 정상가격
# 19,900 원
# 할인율
# 20%
# 판매가격
# 15,900
# 원
# 100g 당 1,325원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (9,678)
# 신선보장
# 장바구니 담기
# 쓱배송
# 요거트 건포도 20g*10입
# 정상가격
# 6,980 원
# 할인율
# 28%
# 판매가격
# 4,980
# 원
# 100g 당 2,490원
# 상품평점 5점 만점에
# 5.0
# 상품평 개수
# (1)
# 장바구니 담기
# 쓱배송
# 새벽배송 가능
# 자연주의 저탄소인증 한라봉 1kg/봉
# 판매가격
# 12,980
# 원
# 상품평점 5점 만점에
# 4.4
# 상품평 개수
# (56)
# 신선보장
# 장바구니 담기
# 쓱배송
# 자연주의 친환경 토마토 900g/팩
# 판매가격
# 8,980
# 원
# 100g 당 998원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (8,402)
# 신선보장
# 장바구니 담기
# 쓱배송
# 제주 그린키위/팩 (1kg내외)
# 정상가격
# 14,800 원
# 할인율
# 13%
# 판매가격
# 12,800
# 원
# 100g 당 1,280원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (3,872)
# 신선보장
# #달달한맛 #쥬스용
# 장바구니 담기
# 쓱배송
# 새벽배송 가능
# 미동농산 건망고 슬라이스 250g
# 판매가격
# 7,980
# 원
# 100g 당 3,192원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (3,424)
# 장바구니 담기
# 쓱배송
# 무지개 방울토마토 600g/팩
# 정상가격
# 9,980 원
# 할인율
# 20%
# 판매가격
# 7,980
# 원
# 100g 당 1,330원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (837)
# 신선보장
# 장바구니 담기
# 쓱배송
# 전주 신고배 4~7입/박스 (3kg)
# 판매가격
# 15,900
# 원
# 100g 당 530원
# 상품평점 5점 만점에
# 4.5
# 상품평 개수
# (5,932)
# 신선보장
# #달달한맛 #제철과일
# 장바구니 담기
# 쓱배송
# 신세계푸드 [필리핀산] 과즙팡팡 컷파인애플 1kg
# 정상가격
# 12,900 원
# 할인율
# 15%
# 판매가격
# 10,900
# 원
# 100g 당 1,090원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (9,141)
# 신선보장
# #달달한맛
# 장바구니 담기
# 쓱배송
# 자연주의 저탄소인증 샤인머스캣 500g/팩
# 판매가격
# 7,980
# 원
# 100g 당 1,596원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (926)
# 신선보장
# 장바구니 담기
# 쓱배송
# 다크초코 건포도 20g*10입
# 정상가격
# 6,980 원
# 할인율
# 28%
# 판매가격
# 4,980
# 원
# 100g 당 2,490원
# 상품평점 5점 만점에
# 5.0
# 상품평 개수
# (1)
# 장바구니 담기
# 쓱배송
# 길림양행 마카다미아 300g
# 판매가격
# 11,800
# 원
# 100g 당 3,934원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (1,701)
# #견과류
# 장바구니 담기
# 쓱배송
# 딸기 500g/팩
# 정상가격
# 19,900 원
# 할인율
# 40%
# 판매가격
# 11,900
# 원
# 100g 당 2,380원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (554)
# 신선보장
# 장바구니 담기
# 쓱배송
# 스미후루 [페루산] 순 유기농 바나나 1묶음 (1.1kg 내외)
# 판매가격
# 4,980
# 원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (22,714)
# 신선보장
# #달달한맛 #아침대용
# 장바구니 담기
# 새벽배송
# [치키타] 과테말라 바나나 (1.2kg/봉)
# 판매가격
# 4,280
# 원
# 100g 당 357원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (24,516)
# 신선보장
# 장바구니 담기
# 쓱배송
# 새벽배송 가능
# 바나나칩 500g
# 판매가격
# 7,980
# 원
# 10g 당 160원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (1,852)
# #간식 #견과류
# 장바구니 담기
# 쓱배송
# 제스프리 제주 골드키위/팩 (900g내외)
# 정상가격
# 19,800 원
# 할인율
# 25%
# 판매가격
# 14,800
# 원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (10,138)
# 신선보장
# #달콤한맛 #골드키위
# 장바구니 담기
# 쓱배송
# [국산의 힘] 김제 금실딸기 500g/팩 (특)
# 정상가격
# 16,100 원
# 할인율
# 20%
# 판매가격
# 12,880
# 원
# 100g 당 2,576원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (1,385)
# 신선보장
# 장바구니 담기
# 쓱배송
# 자연주의 친환경 방울토마토 600g/팩
# 판매가격
# 7,480
# 원
# 100g 당 1,247원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (10,758)
# 신선보장
# #방울토마토
# 장바구니 담기
# 쓱배송
# [국산의 힘] 김제 스마트팜 딸기 750g/팩
# 정상가격
# 19,990 원
# 할인율
# 20%
# 판매가격
# 15,992
# 원
# 100g 당 2,133원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (2,649)
# 신선보장
# #달달한맛
# 장바구니 담기
# 쓱배송
# [국산의 힘] 품평회 대상 감귤 1.8kg/팩
# 판매가격
# 14,900
# 원
# 100g 당 828원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (1,282)
# 신선보장
# 장바구니 담기
# 쓱배송
# [뉴질랜드산] 바로먹는 후숙 아보카도 1개 (300g내외)
# 판매가격
# 1,980
# 원
# 상품평점 5점 만점에
# 4.4
# 상품평 개수
# (100)
# 신선보장
# 장바구니 담기
# 쓱배송
# 방울토마토 600g/팩
# 정상가격
# 8,980 원
# 할인율
# 11%
# 판매가격
# 7,980
# 원
# 100g 당 1,330원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (9,875)
# 신선보장
# #방울토마토
# 장바구니 담기
# 쓱배송
# 청포도향 요거트 레이즌 20g*10입
# 정상가격
# 6,980 원
# 할인율
# 28%
# 판매가격
# 4,980
# 원
# 100g 당 2,490원
# 상품평점 5점 만점에
# 5.0
# 상품평 개수
# (2)
# 장바구니 담기
# 새벽배송
# SSG푸드마켓 SSG 중문 타이벡감귤 3kg/박스
# 정상가격
# 19,900 원
# 할인율
# 30%
# 판매가격
# 13,930
# 원
# 100g 당 465원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (4,247)
# 신선보장
# 프리미엄식품관
# 장바구니 담기
# 쓱배송
# 친환경 제주 참다래 4~6입x2팩 (900g내외)
# 판매가격
# 7,980
# 원
# 100g 당 887원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (1,846)
# 신선보장
# #쥬스용 #아기간식
# 장바구니 담기
# 새벽배송
# SSG푸드마켓 SSG 옥종 한단딸기 500g
# 정상가격
# 19,900 원
# 할인율
# 35%
# 판매가격
# 12,900
# 원
# 100g 당 2,580원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (12,377)
# 신선보장
# 프리미엄식품관
# 장바구니 담기
# 새벽배송
# I`mperfect 당도선별 못난이사과 2.5kg (봉)
# 정상가격
# 25,900 원
# 할인율
# 34%
# 판매가격
# 16,900
# 원
# 100g 당 676원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (48,918)
# 신선보장
# 장바구니 담기
# 쓱배송
# 토마주르토마토 750g/팩
# 정상가격
# 7,980 원
# 할인율
# 25%
# 판매가격
# 5,980
# 원
# 100g 당 798원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (9,461)
# 신선보장
# #다이어트용 #건강간식
# 장바구니 담기
# 쓱배송
# 웰팜 [냉동] 유기농 블루베리 700g
# 판매가격
# 11,980
# 원
# 100g 당 1,712원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (4,552)
# 신선보장
# 장바구니 담기
# 새벽배송
# [Dole] 필리핀 바나나 (1.2kg/봉)
# 판매가격
# 4,580
# 원
# 100g 당 382원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (14,179)
# 신선보장
# 장바구니 담기
# 쓱배송
# 새벽배송 가능
# 동우농산 건블루베리 350g
# 판매가격
# 13,800
# 원
# 100g 당 3,943원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (1,530)
# #달달한맛 #견과류랑같이먹으려고
# 장바구니 담기
# 쓱배송
# 샤인머스캣 1송이 (대/650g내외)
# 판매가격
# 9,900
# 원
# 상품평점 5점 만점에
# 4.3
# 상품평 개수
# (81)
# 신선보장
# 장바구니 담기
# 쓱배송
# 파머스픽 애플토마토 600g/팩
# 판매가격
# 7,980
# 원
# 100g 당 1,330원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (6,600)
# 신선보장
# 장바구니 담기
# 쓱배송
# [페루산] 달콤한 냉동 애플망고 1.2kg
# 판매가격
# 8,990
# 원
# 100g 당 750원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (4,071)
# 장바구니 담기
# 쓱배송
# [미국산] 레몬 7~10입/봉 (1.2kg)
# 판매가격
# 8,980
# 원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (48)
# 신선보장
# 장바구니 담기
# 새벽배송
# 제주 중문 노지감귤 5kg/박스
# 정상가격
# 29,900 원
# 할인율
# 40%
# 판매가격
# 17,940
# 원
# 100g 당 359원
# 상품평점 5점 만점에
# 4.4
# 상품평 개수
# (203)
# 신선보장
# 장바구니 담기
# 새벽배송
# SSG푸드마켓 SSG 톡톡 대추방울토마토 500g/팩
# 판매가격
# 4,980
# 원
# 100g 당 996원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (651)
# 신선보장
# 프리미엄식품관
# 장바구니 담기
# 쓱배송
# 자연주의 저탄소인증 배 3~4입/봉 (2kg내외)
# 판매가격
# 12,980
# 원
# 100g 당 649원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (1,913)
# 신선보장
# 장바구니 담기
# 쓱배송
# 파머스픽 신고배 2입/봉 (1.4kg)
# 판매가격
# 11,980
# 원
# 100g 당 856원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (333)
# 신선보장
# 장바구니 담기
# 새벽배송
# 칠레산 생블루베리 310g (팩)
# 정상가격
# 15,800 원
# 할인율
# 37%
# 판매가격
# 9,800
# 원
# 100g 당 3,162원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (5,227)
# 신선보장
# #아이간식 #어린이간식
# 장바구니 담기
# 쓱배송
# 신세계푸드 [호주산] 네이블 오렌지 8~10입/봉 (2kg내외)
# 판매가격
# 9,980
# 원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (407)
# 신선보장
# 장바구니 담기
# 쓱배송
# [브라질산] 애플망고 2입/팩 (900g내외)
# 정상가격
# 17,980 원
# 할인율
# 22%
# 판매가격
# 13,980
# 원
# 상품평점 5점 만점에
# 4.5
# 상품평 개수
# (35)
# 신선보장
# 장바구니 담기
# 새벽배송
# 고당도 샤인머스켓 1.5kg(박스)
# 정상가격
# 29,900 원
# 할인율
# 33%
# 판매가격
# 19,900
# 원
# 100g 당 1,327원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (8,668)
# 신선보장
# 장바구니 담기
# 쓱배송
# 찰토마토 1.2kg/팩
# 판매가격
# 11,800
# 원
# 100g 당 984원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (19,951)
# 신선보장
# #톰매이 #다이어트용
# 장바구니 담기
# 새벽배송
# 호주산 네이블 오렌지 1.4kg (5~8입/봉)
# 정상가격
# 9,800 원
# 할인율
# 10%
# 판매가격
# 8,800
# 원
# 100g 당 629원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (6,546)
# 신선보장
# #간식
# 장바구니 담기
# 새벽배송
# [기획] 서귀포 실속 감귤 3.8kg (박스)
# 정상가격
# 20,900 원
# 할인율
# 28%
# 판매가격
# 14,900
# 원
# 100g 당 393원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (17,674)
# 신선보장
# 장바구니 담기
# 새벽배송
# 완숙토마토 1.2kg(팩)
# 정상가격
# 12,900 원
# 할인율
# 23%
# 판매가격
# 9,900
# 원
# 100g 당 825원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (4,626)
# 신선보장
# 장바구니 담기
# 새벽배송
# 유명산지 샤인머스켓 2kg (박스)
# 정상가격
# 34,900 원
# 할인율
# 28%
# 판매가격
# 24,900
# 원
# 100g 당 1,245원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (7,285)
# 신선보장
# 2+1
# 장바구니 담기
# 쓱배송
# 테일러푸룬 유기농 테일러푸룬 건자두 210g
# 판매가격
# 6,980
# 원
# 100g 당 3,324원
# 상품평점 5점 만점에
# 4.8
# 상품평 개수
# (5,061)
# #변비예방용 #간식
# 장바구니 담기
# 쓱배송
# dole [베트남산] 용과 1개 500g내외
# 판매가격
# 3,980
# 원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (2,027)
# 신선보장
# #아이간식 #달달한맛
# 장바구니 담기
# 쓱배송
# dole [필리핀산] Dole 바나나 1kg내외
# 판매가격
# 4,980
# 원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (18,063)
# 신선보장
# 장바구니 담기
# 쓱배송
# 파머스픽 새콤아삭 컬러마토 750g/팩
# 판매가격
# 7,980
# 원
# 100g 당 1,064원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (4,932)
# 신선보장
# 장바구니 담기
# 새벽배송
# [당도선별] 유명산지 청송사과 1.5kg (봉)
# 정상가격
# 19,900 원
# 할인율
# 15%
# 판매가격
# 16,900
# 원
# 100g 당 1,127원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (144,185)
# 신선보장
# #유명산지
# 장바구니 담기
# 새벽배송
# 농협 I`mperfect 당도선별 못난이사과 2kg (봉)
# 정상가격
# 23,800 원
# 할인율
# 37%
# 판매가격
# 14,800
# 원
# 100g 당 740원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (8,245)
# 신선보장
# 장바구니 담기
# 쓱배송
# 친환경 대추방울토마토 600g/팩
# 판매가격
# 7,780
# 원
# 100g 당 1,297원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (6,267)
# 신선보장
# #방울토마토 #대추방울토마토
# 1+1
# 장바구니 담기
# 새벽배송
# 아삭아삭 단감 5입 870g (봉)
# 판매가격
# 15,000
# 원
# 100g 당 1,725원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (9,808)
# 신선보장
# #아삭아삭
# 장바구니 담기
# 새벽배송
# [당도선별] 유명산지 사과 1.3kg (봉)
# 정상가격
# 17,900 원
# 할인율
# 16%
# 판매가격
# 14,900
# 원
# 100g 당 1,147원
# 상품평점 5점 만점에
# 4.5
# 상품평 개수
# (1,355)
# 신선보장
# 장바구니 담기
# 새벽배송
# 무농약 한단딸기 500g/팩 (특)
# 판매가격
# 13,980
# 원
# 100g 당 2,796원
# 상품평점 5점 만점에
# 4.6
# 상품평 개수
# (6,593)
# 신선보장
# #쥬스용 #달달한맛
# 장바구니 담기
# 새벽배송
# 제주산 제스프리 골드키위 10 ~12입 1.3kg (팩)
# 정상가격
# 24,800 원
# 할인율
# 28%
# 판매가격
# 17,800
# 원
# 100g 당 1,370원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (1,457)
# 신선보장
# #골드키위
# 장바구니 담기
# 입고예정
# 입고알림
# 대체상품 팝업 열기
# 장바구니 담기
# 쓱배송
# 딸기 500g/팩
# 정상가격
# 19,900 원
# 할인율
# 40%
# 판매가격
# 11,900
# 원
# 100g 당 2,380원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (24,876)
# 신선보장
# #달달한맛 #제철과일
# 장바구니 담기
# 입고예정
# 입고알림
# 대체상품 팝업 열기
# 장바구니 담기
# 새벽배송
# [당도선별] 서귀포감귤 3kg (박스)
# 정상가격
# 19,800 원
# 할인율
# 35%
# 판매가격
# 12,800
# 원
# 100g 당 427원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (46,953)
# 신선보장
# 장바구니 담기
# 입고예정
# 입고알림
# 대체상품 팝업 열기
# 장바구니 담기
# 새벽배송
# 유명산지 설향딸기 500g (팩)
# 정상가격
# 19,900 원
# 할인율
# 35%
# 판매가격
# 12,900
# 원
# 100g 당 2,580원
# 상품평점 5점 만점에
# 4.7
# 상품평 개수
# (30,191)
# 신선보장