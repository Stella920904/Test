from Modules import *
from CommonLogin import *


class TC_PaymentsAdd_Class():
    CommonloginClass()
#결제수단 추가
    try:
        # GNN Menu Open  
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[3]/img').click()
        time.sleep(settings.sec)
        # 결제관리 Menu 선택
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[2]/div[5]').click()
        time.sleep(settings.sec)
        # 카드 추가 Side Modal open
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[2]/div/div').click()
        time.sleep(settings.sec)
        # 카드 정보 등록 > 카드번호
        driver.find_element(By.XPATH, '//*[@id="side-modal"]/form/div[2]/div/div/div[2]/input').send_keys(settings.cardNumber) 
        time.sleep(settings.sec)
        driver.find_element(By.XPATH, '//*[@id="side-modal"]/form/div[3]/button').click()
        time.sleep(settings.sec)
        # 카드 정보 등록 > 유효기간, CVC, 생년월일
        driver.find_element(By.XPATH, '//*[@id="side-modal"]/form/div[2]/div/div[1]/div[2]/input').send_keys(settings.expiredDate) 
        driver.find_element(By.XPATH, '//*[@id="side-modal"]/form/div[2]/div/div[2]/div[2]/input').send_keys(settings.cvcNumber)
        driver.find_element(By.XPATH, '//*[@id="side-modal"]/form/div[2]/div/div[3]/div[2]/input').send_keys(settings.birthDate)
        time.sleep(settings.sec)
        driver.find_element(By.XPATH, '//*[@id="side-modal"]/form/div[3]/button[2]').click()
        time.sleep(settings.sec)
        if driver.current_url == 'https://qa-console.surffy-dev.io/ko/home/payment_management/method':
            print('카드등록 성공')
            settings.Passcount = settings.Passcount + 1
        else:
            print('카드등록 실패') # 오류모달로 인한 실패 코드 작성 필요
            settings.FailCount = settings.FailCount + 1
    except:
        print('요소를 찾을 수 없어 카드등록 실패')
    
print("PassCount :", settings.Passcount)
print("FailCount :", settings.FailCount)
driver.quit()