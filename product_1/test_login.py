import pytest
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from conftest import browser_with_login, handle_fail, error_file_path
import os

load_dotenv()
test_login_id = os.getenv("LOGIN_ID")

def test_case_1_1(browser_with_login, error_file_path):
    with handle_fail(browser_with_login, error_file_path):
        selected_text = browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[1]').text
        specified_text = "안녕하세요, " + test_login_id +"님!"
        print(selected_text)
        assert selected_text == specified_text

