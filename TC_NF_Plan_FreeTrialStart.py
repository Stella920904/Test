from Modules import *
from CommonLogin import *

#chromedriver 경로 설정
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--start-maximized')
# driver = webdriver.Chrome(ChromeDriverManager().install())

class TC_NF_Plan_FreeTrialStart_Class():
    print("FreeTrial 테스트 시작!")
    #Login 함수 호출
    def test(self):
        Commonlogintest = CommonloginClass
        Commonlogintest.CommonloginDef()

    def FreetrialStart(self):
    #FreeTrial 테스트 시작
        try:
            # Free Trial 시작하기
            driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]/button').click()
            time.sleep(settings.sec)
            # 시작하기 Modal
            driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/button').click()
            time.sleep(600)
            # Free Trial 플랜 선택
            driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]').click()
            time.sleep(settings.sec)
            if driver.current_url == 'https://qa-console.surffy-dev.io/ko/console/product/nf/home':
                print('Free Trial 시작 성공')
                settings.Passcount = settings.Passcount + 1
            else:
                print('Free Trial 시작 실패')
                settings.FailCount = settings.FailCount + 1
            print("PassCount :", settings.Passcount)
            print("FailCount :", settings.FailCount)
            print("FreeTrial 테스트 종료!")
            driver.quit()
        except:
            print('요소를 찾을 수 없어 Free Trial 플랜 시작하기 실패')
            driver.quit()
            
freetest = TC_NF_Plan_FreeTrialStart_Class()
freetest.FreetrialStart()

