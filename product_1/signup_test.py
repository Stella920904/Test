import pytest
from selenium.webdriver.common.by import By
from conftest import browser_with_signup, handle_fail, error_file_path

def test_case_2_1(browser_with_signup, error_file_path):
    with handle_fail(browser_with_signup, error_file_path):
        selected_text = browser_with_signup.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]/div/div[1]').text
        specified_text = "Surffy의 가상 대기실 솔루션을 알아보세요."
        
        assert selected_text == specified_text



