import pytest
from selenium import webdriver
from contextlib import contextmanager
from selenium.webdriver.common.by import By
import datetime
import time 
from dotenv import load_dotenv
from browser_setup import browser
import os

# 환경 변수 불러오기 (테스트 세팅값 불러오기)
load_dotenv()
test_login_url = os.getenv("LOGIN_URL")
test_login_id = os.getenv("LOGIN_ID")
test_login_pw = os.getenv("LOGIN_PW")
test_signup_url = os.getenv("SIGNUP_URL")



def pytest_collection_modifyitems(config, items):
     # items 리스트를 원하는 순서로 조작
    # items.reverse()  # 역순으로 실행
    # 혹은 items 리스트를 원하는 기준으로 정렬
    items.sort(key=custom_sort_key_function)
    # 필요한 조작을 통해 items 리스트를 조작
    # ...
    # items 리스트 출력
    for item in items :
        print("module : ", item.parent.name, item.name )

def custom_sort_key_function(item):
    # item은 pytest에서 수집한 테스트 항목을 나타내는 객체입니다
    # item에는 테스트 함수/메서드의 정보와 테스트 파일 이름 등이 포함되어 있습니다
    # 원하는 방식으로 item을 비교하여 정렬하기 위한 정렬 키를 반환하는 함수를 작성합니다
    module_name = item.parent.name  # 테스트 파일의 이름
    test_name = item.name  # 테스트 함수/메서드의 이름
    if test_name == "test_case_2_1":
        return 1
    elif "test_createproject" in module_name and test_name.startswith("test_case_1"):
        return 2
    elif "test_nfmain" in module_name and test_name.startswith("test_case_1"):
        return 3
    elif "test_login" in module_name and test_name.startswith("test_case_1"):
        return 4
    elif "test_freetrialstart" in module_name and test_name.startswith("test_case_1"):
        return 5
    else:
        return 0


# 재사용되는 페이지들 !!
# scope가 모듈일 경우 모듈 단위로 재사용함.

# 로그인 함수 호출
@pytest.fixture(scope="module")
def browser_with_login(browser):
    console_url = test_login_url
    login_id = test_login_id
    login_pw = test_login_pw

    browser.get(console_url)
    browser.find_element(By.NAME, 'email').send_keys(login_id)
    browser.find_element(By.NAME, 'password').send_keys(login_pw)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button').click()    
    time.sleep(3)
    yield browser

# nf 메인 진입 함수 호출
@pytest.fixture(scope="module")
def browser_with_nfmain(browser_with_login):
    browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]').click()
    time.sleep(3)
    yield browser_with_login

# mf 메인 > 프로젝트 생성
@pytest.fixture(scope="function")
def browser_with_createproject(browser_with_login):
    browser_with_login.get("https://qa-console.surffy-dev.io/ko/console/product/nf/home")
    time.sleep(1)
    browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[4]/div[1]/div[2]/button').click()
    time.sleep(1)
    browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[1]/div[3]/div[2]/input').send_keys("stclab.com")
    time.sleep(1)
    browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[2]/div[2]/div[2]/input').send_keys("api")
    time.sleep(1)
    browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button').click()
    time.sleep(3)
    yield browser_with_createproject

# 에이전트 설치 스크립트
@pytest.fixture(scope="function")
def browser_with_installagent(browser_with_createproject):
    browser_with_createproject.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[3]/div[2]/div[1]').click()
    browser_with_createproject.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[3]/div[3]/button').click()
    browser_with_createproject.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[4]/button[2]').click()
    yield browser_with_createproject


# 회원가입 함수 호출
@pytest.fixture(scope="module")
def browser_with_signup(browser):
    console_url = test_signup_url
    login_id = test_login_id
    login_pw = test_login_pw
    
    browser.get(console_url)
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[1]/div[2]/button').click()                   # 국가
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[1]/div[2]/ul/li[1]/button').click()          # 대한민국 선택
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[2]/div[2]/button').click()                   # 지역
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[2]/div[2]/ul/li/button').click()             # 서울 선택
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[3]/div[2]/input').click()                    # 이메일 영역 선택
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[3]/div[2]/input').send_keys(login_id)         # 이메일 입력
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[4]/div[2]/input').send_keys(login_id)          # 이름 입력              
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[5]/div[2]/input').send_keys(login_id)          # 회사명 입력
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[6]/div[2]/input').click()                    # 비밀번호 입력영역 선택
    time.sleep(1)                                                                                             
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[6]/div[2]/input').send_keys(login_pw)        # 비밀번호 입력
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[7]/div[2]/input').click()                    # 비밀번호 확인 입력영역 선택
    time.sleep(1)                                                                                                      
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[7]/div[2]/input').send_keys(login_pw)        # 비밀번호 확인 입력
    browser.find_element(By.XPATH, '//*[@id="terms"]').click()                                                                     # 동의하기 선택
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button').click()                                     # 회원가입 버튼 클릭
    time.sleep(3)
    yield browser

#Surffy 메인 시작
@pytest.fixture(scope="module")
def browser_with_surffymain(browser_with_login):
    browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]/button').click()
    time.sleep(1)
    browser_with_login.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/button').click()
    time.sleep(600)
    browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]').click()
    time.sleep(3)
    yield browser_with_login



#


# 아래는 테스트 관련 설정!!
# 딱히 수정안해도 됨

# 스크린샷 파일 명 설정 (Test Case 함수 명으로)
@pytest.fixture(scope="function", autouse=True)
def error_file_path(request):
    file_path = f'./screenshots/{datetime.datetime.now().strftime("%m%d%H%M")}_{request.node.name}.png'
    yield file_path

# Assert 에러(검증 코드가 틀렸을때) OR 코드 자체 에러 (html 요소가 없을 때 등) fail 처리
@contextmanager
def handle_fail(browser, error_file_path):
    try:
        yield
    except AssertionError:
        print(error_file_path)
        browser.save_screenshot(error_file_path)
        pytest.fail("Assertion error occurred")
    except Exception:
        browser.save_screenshot(error_file_path)
        pytest.fail("Exception occurred")
