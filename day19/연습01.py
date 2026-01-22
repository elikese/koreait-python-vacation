from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

url = "https://www.naver.com"

# 파이썬이 내pc를 사용해서 브라우저를 열고 행동

# 크롬 설치파일 가져오기
driver_manager = ChromeDriverManager().install()
# 셀레니움에 설치
chrome_service = Service(driver_manager)
# 인터넷창(브라우저) 생성
driver = webdriver.Chrome(service=chrome_service)

# local_list에 있는 지역온도를 셀레니움으로
# 네이버에 검색하여서 출력해 주세요
local_list = ["부산","대구","대전","인천","서울","광주","울산"]

# 네이버에 접속해서 "부산날씨"검색결과 페이지 접속
# copy -> copy selector

for local in local_list:
    driver.get(url)
    sleep(1)
    input_tag = driver.find_element(By.CSS_SELECTOR, "#query")
    input_tag.send_keys(f"{local} 날씨")
    sleep(0.5)
    # 버튼찾기
    search_btn_tag = driver.find_element(By.CSS_SELECTOR, "#sform > fieldset > button")
    search_btn_tag.click()
    sleep(2)
    temp_tag = driver.find_element(By.CSS_SELECTOR, "#main_pack > section > div > div:nth-child(1) > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.weather_graphic > div.temperature_text > strong")
    temperature = temp_tag.text
    print(f"현재 {local}: {temperature.strip()[5:].strip()}")

