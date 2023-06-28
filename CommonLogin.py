from Modules import *
from GetDriver import driver
# #chromedriver 경로 설정
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--start-maximized')


class CommonloginClass():
    def CommonLoginDef(self):
        driver.get(Settings.loginurl)
        try:
            driver.find_element(By.NAME, 'email').send_keys(Settings.consoleid)
            driver.find_element(By.NAME, 'password').send_keys(Settings.password)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button').click()
            time.sleep(5)

        #     if driver.current_url == 'https://qa-console.surffy-dev.io/ko/home':
        #         print('로그인 성공')
        #         Settings.passcount = Settings.passcount + 1
        #     else:
        #         print('로그인 실패')
        #         Settings.failcount = Settings.failcount + 1
        except:
            print('요소를 찾을 수 없어 로그인 실패')
         

    # print("passcount :", Settings.passcount)
    # print("failcount :", Settings.failcount)

# CommonloginClassGo = CommonloginClass()
# CommonloginClassGo.CommonloginDef()
