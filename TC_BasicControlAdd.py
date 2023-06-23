import selenium.webdriver.support.ui as ui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# #chromedriver 경로 설정
# CHROMEDRIVER_PATH = 'chromedriver.exe'
# chrome_options = Options()
# chrome_options.add_argument('--start-maximized')

#URL info
loginurl = "https://qa-console.surffy-dev.io/ko/signin/"
basic = "https://qa-console.surffy-dev.io/ko/byol/console/product/nf/65/controls/basic/default"
segURL = "http://heart.stclab.com:5004/"

#진입
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(loginurl)

#sleep 시간
sec = 1

#세그먼트 반복 수
segCount = 20

#login info
consoleid = 'qa_kade016@stclab.com'
password = 'qwe123!!'

#로그인
driver.find_element(By.NAME, 'email').send_keys(consoleid)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button').click()
time.sleep(sec)

#콘솔 홈
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]').click()
time.sleep(sec)

#프로젝트 선택
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[4]/div[2]/div/div').click()
time.sleep(sec)

#기본제어 진입
# driver.find_element(By.XPATH, '').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[1]/div[2]/div[2]/div[2]').click()
time.sleep(sec)

#기본제어 모달 생성 반복문
for num in range(segCount):
    # 세그먼트 명을 string 으로 반환
    segnameArr = ["test2", num]
    segname = ''.join(str(s) for s in segnameArr)
    # URL을 string 으로 반환
    segurlArr = [segURL, num]
    segurlname = ''.join(str(s) for s in segurlArr)
    #모달저장
    driver.find_element(By.CLASS_NAME, 'css-phyh84').click()
    time.sleep(sec)
    driver.find_element(By.XPATH, '//*[@id="side-modal"]/form[1]/div[2]/div[1]/div[2]/input').send_keys(segname)
    driver.find_element(By.XPATH, '//*[@id="side-modal"]/form[1]/div[2]/div[3]/div[2]/input').send_keys(segurlname)
    driver.find_element(By.XPATH, '//*[@id="side-modal"]/form/div[2]/div[9]/div[2]/input').send_keys(num)
    driver.find_element(By.XPATH, '//*[@id="side-modal"]/form[1]/div[3]/button').click()
    driver.find_element(By.XPATH, '//*[@id="side-modal"]/div[3]/div[2]/button[2]').click()
    time.sleep(sec)
time.sleep(1000)
driver.close