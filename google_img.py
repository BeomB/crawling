from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(2)

email = 'gowjr1119@daum.net' 
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = '1119beomki' 
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()
time.sleep(7)
try:
    driver.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF').click()
except:
    print("하하")
time.sleep(5)
try:
    driver.find_element_by_css_selector('button.aOOlW.HoLwm').click()
except:
    print("하하")
search = "남성 탈모" #검색할 키워드
time.sleep(2)
elem = driver.find_element_by_css_selector('input.XTCLo.x3qfX')
elem.send_keys(search)
time.sleep(3)
driver.find_element_by_css_selector('div.z556c').click()
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
print("하하2")
print(len(images))
print("하하1")
for image in images:
    try:
        time.sleep(3)
        print("하하2")
        imgUrl= driver.find_elements_by_css_selector("img.FFVAD")[count].get_attribute("src")
        #imgUrl=image[count].get_attribute("src")
        print("glgl")
       # driver.find_elements_by_css_selector(".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl,str(count)+".jpg")
        count = count+1
    except:
        pass
    










# driver.get("https://www.instagram.com/")
# elem = driver.find_element_by_name("username")
# elem.send_keys("gowjr1119@daum.net")
# elem1 = driver.find_element_by_name("password")
# elem1.send_keys("1119beomki")
# # elem1.send_keys(Keys.RETURN)



# #스크롤 내리는거
# SCROLL_PAUSE_TIME = 1

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try:
#             driver.find_elements_by_css_selector(".mye4qd").click()
#         except:
#             break
            
#     last_height = new_height

# #스크롤 다 내림

# images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# count =1
# for image in images:
#     try:
#         image.click()
#         time.sleep(3) 
#         imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
#         # driver.find_elements_by_css_selector(".n3VNCb").get_attribute("src")
#         urllib.request.urlretrieve(imgUrl,str(count)+".jpg")
#         count = count+1
#     except:
#         pass


# driver.close()