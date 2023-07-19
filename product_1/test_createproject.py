import pytest
from selenium.webdriver.common.by import By
from conftest import browser_with_createproject, browser_with_installagent, handle_fail, error_file_path

def test_case_1_1(browser_with_createproject, error_file_path):
    with handle_fail(browser_with_createproject, error_file_path):
        selected_text = browser_with_createproject.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/div[1]').text
        specified_text = "에이전트 설치"
        assert selected_text == specified_text

def test_case_1_2(browser_with_installagent, error_file_path):
    with handle_fail(browser_with_installagent, error_file_path):
        selected_text = browser_with_installagent.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[4]/div[2]/div/div/ul/li[1]/div/div/div[1]').text
        specified_text = "api"
        assert selected_text == specified_text