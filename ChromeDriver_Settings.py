import selenium.webdriver.support.ui as ui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from Settings import *

class chromedriver_settings:
    def chromedriverSettings():
        #chromedriver 경로 설정
        chrome_options = webdriver_manager.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        
