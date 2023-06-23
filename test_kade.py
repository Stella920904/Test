from Modules import *

#chromedriver 경로 설정
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(settings.loginurl)
time.sleep(5)