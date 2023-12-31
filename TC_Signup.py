from Modules import *

# 테스트계정 입력
account = input("테스트 계정을 입력해 주세요 : ")

#chromedriver 경로 설정
# chrome_options = Options()
# chrome_options.add_argument('--start-maximized')

# 브라우저 실행 및 탭 추가
driver = webdriver.Chrome(ChromeDriverManager().install())


class TC_Signup_Class():
    driver.get(settings.signupurl)                                                                                                    # 콘솔 url 회원가입 페이지 열기         #  회원가입 클릭
    time.sleep(settings.sec)
  
    try:
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[1]/div[2]/button').click()                   # 국가
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[1]/div[2]/ul/li[1]/button').click()          # 대한민국 선택
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[2]/div[2]/button').click()                   # 지역
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[2]/div[2]/ul/li/button').click()             # 서울 선택
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[3]/div[2]/input').click()                    # 이메일 영역 선택
        time.sleep(settings.sec)

        # 이메일 명을 string 으로 반환
        # emailArr = f"auto_kade{settings.num+1}@stclab.com"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[3]/div[2]/input').send_keys(account)         # 이메일 입력
        # nameArr = f"auto_kade{settings.num+1}@stclab.com"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[4]/div[2]/input').send_keys(account)          # 이름 입력
        # comName = f"auto_kade{settings.num+1}@stclab.com"              
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[5]/div[2]/input').send_keys(account)          # 회사명 입력
        time.sleep(settings.sec)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[6]/div[2]/input').click()                    # 비밀번호 입력영역 선택
        emailPW1 = 'qwe123!!'
        time.sleep(settings.sec)                                                                                                               # 비밀번호 qwe123!! 로 설정
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[6]/div[2]/input').send_keys(emailPW1)        # 비밀번호 입력
        time.sleep(settings.sec)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[7]/div[2]/input').click()                    # 비밀번호 확인 입력영역 선택
        emailPW2 = 'qwe123!!'
        time.sleep(settings.sec)                                                                                                               # 비밀번호와 동일하게 설정
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[7]/div[2]/input').send_keys(emailPW2)        # 비밀번호 확인 입력
        time.sleep(settings.sec)
        driver.find_element(By.XPATH, '//*[@id="terms"]').click()                                                                     # 동의하기 선택
        time.sleep(settings.sec)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button').click()                                     # 회원가입 버튼 클릭
        time.sleep(5)
        if driver.current_url == 'https://qa-console.surffy-dev.io/ko/home':
            print('로그인 성공')
            settings.Passcount = settings.Passcount + 1
        else:
            print('로그인 실패')
            settings.FailCount = settings.FailCount + 1
    except:
        print('요소를 찾을 수 없어 로그인 실패')
    print("PassCount :", settings.Passcount)
    print("FailCount :", settings.FailCount)
driver.quit()