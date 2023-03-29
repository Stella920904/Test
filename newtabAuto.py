import selenium.webdriver.support.ui as ui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
 
#chromedriver 경로 설정
CHROMEDRIVER_PATH = 'chromedriver.exe'
 
chrome_options = Options()
chrome_options.add_argument('--start-maximized')
 
 
#브라우저 실행 및 탭 추가
driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
driver.execute_script('window.open("about:blank", "_blank");')
driver.execute_script('window.open("about:blank", "_blank");')
driver.execute_script('window.open("about:blank", "_blank");')
driver.execute_script('window.open("about:blank", "_blank");')
 
tabs = driver.window_handles
 
# TAB_1
driver.switch_to.window(tabs[0])
driver.get('http://heart.stclab.com:5002')
button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/button')
button1.click()
# time.sleep(3)

# TAB_2
driver.switch_to.window(tabs[1])
driver.get('http://heart.stclab.com:5002')
button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/button')
button1.click()
# time.sleep(3)

# TAB_3
driver.switch_to.window(tabs[2])
driver.get('http://heart.stclab.com:5002')
button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/button')
button1.click()
# time.sleep(3)

driver.switch_to.window(tabs[3])
driver.get('http://heart.stclab.com:5002')
button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/button')
button1.click()
# time.sleep(3)

driver.switch_to.window(tabs[4])
driver.get('http://heart.stclab.com:5002')
button1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/button')
button1.click()
time.sleep(1000)
