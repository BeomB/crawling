from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome("/Users/beom/Documents/Code/crawling/chromedriver")
driver.get("https://www.instagram.com/")
time.sleep(2)

email = 'gowjr119@daum.net' 
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = '' 
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()
time.sleep(3)
try:
    driver.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF').click()
except:
    print("하하")
time.sleep(2)
print("로그인 완료")
try:
    driver.find_element_by_css_selector('button.aOOlW.HoLwm').click()
except:
    print("하하")
search = "#한라산정상1950m" #검색할 키워드
time.sleep(2)
elem = driver.find_element_by_css_selector('input.XTCLo.d_djL.DljaH')
elem.send_keys(search)
time.sleep(3)
print("검색 완료")
driver.find_element_by_css_selector('div._7UhW9.xLCgt.qyrsm.KV-D4.uL8Hv').click()
#스크롤 내리는거
SCROLL_PAUSE_TIME = 1
# # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
timer = 1
while (timer<5):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    timer=timer+1

count =0
images = driver.find_elements_by_css_selector("img.FFVAD")
print(len(images))
time.sleep(4)

for image in images:
    print("확인2")
    try:
        print("확인3")
        time.sleep(4)
        print("확인4")
        imgUrl= driver.find_elements_by_css_selector("img.FFVAD")[count].get_attribute("src")
        print("다운로드 시작")
        urllib.request.urlretrieve(imgUrl,str(count)+".jpg")
        print("다운로드 완료")
        count = count+1
    except:
        pass
        
    
# elem.send_keys("gojr1119@daum.net")
# elem1.send_keys("1119beomki")