from urllib.request import urlopen
from urllib.parse import quote_plus # 아스키 코드로 변환시켜준다.
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# 변수 url 에 저장될 url 형식은 아래와 같다.
# https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%9C%A0/

# baseUrl은 검색하기 전의 베이스가 되는 url이다.
baseUrl = 'https://www.instagram.com/explore/tags/'
#plusUrl은 input으로 검색어를 받아서 아래에서 baseUrl에 추가되는 url이다.
plusUrl = input('검색할 태그를 입력하세요 : ')
#plusUrl로 받아온 검색어를 quote_plus 모듈로 아스키 코드로 변환시킨 뒤, url에 저장시킨다.
url = baseUrl + quote_plus(plusUrl)

# 인스타그램의 페이지 소스를 보면 대부분 JavaScript다. 그래서 selenium 의 webdriver 가 필요하다.
# beautifulSoup로 JavaScript로 되어있는 사이트는 크롤링 할 수 없다.

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url) # 드라이버를 띄운다. (크롬 웹 페이지를 연다.)

# selenium 은 기본적으로 느리다.
# 만약 속도가 매우 느리다면 사진이 하나하나씩 뜨는 경우가 생길 수 있으므로 사진이 다 뜨기 전에
# 창이 닫히는 경우를 방지하기 위해 드라이버를 띄우고 나서 3초를 기다려 준다.
# 여기서 3초를 기다린 다음에 아래에서 페이지 소스(이미지)들을 불러오기 시작한다.
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

# select는 페이지에 있는 정보를 다 가져 온다.
# 클래스가 여러 개면 기존 클래스의 공백을 없애고 .으로 연결시켜 주어야 한다.
insta = soup.select('.v1Nh3.kIKUG._bz0w')

n = 1

# 이미지 하나만 가져올 게 아니라 여러 개를 가져올 것이므로 반복문을 쓴다.
for i in insta:
    # 인스타 주소에 i번 째의 a태그의 href 속성을 더하여 출력한다.
    print('https://www.instagram.com' + i.a['href'])
    # 인스타 페이지 소스에서 이미지에 해당하는 클래스의 이미지 태그의 src 속성을 imgUrl에 저장한다.
    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:
        # img라는 폴더 안에 programmer(n).jpg 파일을 저장한다.
        # 텍스트 파일이 아니기 때문에 w(write)만 쓰면 안되고 binary 모드를 추가시켜야 한다.
        with open('./img/' + plusUrl + str(n) + '.jpg', "wb") as h:
            # f를 읽고 img에 저장한다.
            img = f.read()
            # h에 위 내용을 쓴다.
            h.write(img)
    # 계속 programmer 1에 덮어쓰지 않도록 1을 증가시켜 준다
    n += 1 
    print(imgUrl)
    # 출력한 걸 보았을 때 구분하기 좋도록 빈 줄을 추가시킨다.
    print()
# 마지막에 driver를 닫아준다. (열린 창을 닫는다.)     
driver.close()
    
# 우리가 인스타 페이지에 들어가서 스크롤 하기 전까지 보여진 사진 개수가 img 폴더에 저장된다.

# sns의 경우는 스크롤 기능이 빈번하기 때문에 JavaScript로 되어있는 경우가 많다.

# JavaScript 로 되어있는 사이트를 크롤링하려면 selenium 이 유용하다.

# 하지만 selenium은 속도가 느리기 때문에 JavaScript로 되어있는 사이트가 아닌 경우라면
# beautifulSoup 가 더 선호된다.

# 대신 터미널에서 어떤 내용이 진행되고 있는지 눈으로 보고 싶다면 selenium 을 쓰면 좋다. 