from Modules import *
from GetDriver import driver
# #chromedriver 경로 설정
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--start-maximized')

class TC_login_Class():
    def login_def():
        print('로그인 테스트 시작!')
        driver.get(Settings.loginURL)
        try:
            driver.find_element(By.NAME, 'email').send_keys(Settings.consoleid)
            driver.find_element(By.NAME, 'password').send_keys(Settings.password)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button').click()
            time.sleep(Settings.sec)

            if driver.current_url == 'https://qa-console.surffy-dev.io/ko/home':
                print('로그인 성공')
                Settings.passcount = Settings.passcount + 1
            else:
                print('로그인 실패')
                Settings.failcount = Settings.failcount + 1
        except:
            print('요소를 찾을 수 없어 로그인 실패')
        
        finally:
            print("passcount :", Settings.passcount)
            print("failcount :", Settings.failcount)
            driver.quit()
            print('로그인 테스트 종료!')

# loginTest = TC_login_Class()
# loginTest.def_login()



