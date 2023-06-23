import selenium.webdriver.support.ui as ui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

# Pageload Strategy 설정 변경(성능)
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"

# chromedriver 경로 설정
CHROMEDRIVER_PATH = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--start-maximized')

# 반복할 호출 수
count = 20

# sleep 시간
sec = 1000000

# API버튼정의
alertbutton = '//*[@id="__next"]/div/div[1]/div/div/div[2]/a[4]'
buttons = '//*[@id="__next"]/div/div[1]/div/div/div[2]/a[2]'
pagenation = '//*[@id="__next"]/div/div[1]/div/div/div[2]/a[7]'

# XHR버튼정의
XHRbutton1 = '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[4]/div/div[1]/div/div/button'
XHRbutton2 = '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/button'
XHRbutton3 = '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[4]/div/div[3]/div/div/button'

# 브라우저 실행 및 탭 추가
driver = webdriver.Chrome(ChromeDriverManager().install())
for dirver in range(count):
    driver.execute_script('window.open("about:blank", "_blank");')
    tabs = driver.window_handles

# 탭 핸들링
for num in range(count):
    # TAB_num
    driver.switch_to.window(tabs[num])
    driver.get('http://heart.stclab.com:5201')
    # driver.get('http://heart.stclab.com:5102')
    # driver.get('http://heart.stclab.com:5202')


    # API 구간제어 Alert 버튼
    button = driver.find_element(By.XPATH,pagenation)
    driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    print(num+1,'번째 호출 완료')
print('url 부하 테스트 완료')
time.sleep(sec)
driver.quit