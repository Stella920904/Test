from Modules import *
from CommonLogin import *

#chromedriver 경로 설정
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--start-maximized')
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(ChromeDriverManager().install())

class TC_NF_Plan_Upgade_Class():
    CommonloginClass()

# NF Free Trial 플랜 Upgrade
    try:
        # Upgrade 시작하기
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[3]/button').click()
        time.sleep(Settings.sec)
        # Samll 플랜으로 변경
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[1]/div[1]/div[3]/button').click()
        time.sleep(600)
        # Free Trial 플랜 선택
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]').click()
        time.sleep(Settings.sec)
        if driver.current_url == 'https://qa-console.surffy-dev.io/ko/console/product/nf/home':
            print('로그인 성공')
            Settings.passcount = Settings.passcount + 1
        else:
            print('로그인 실패')
            Settings.failcount = Settings.failcount + 1
    except:
        print('요소를 찾을 수 없어 로그인 실패')

    print("passcount :", Settings.passcount)
    print("failcount :", Settings.failcount)
driver.quit()