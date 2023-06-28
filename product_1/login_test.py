import pytest
from selenium.webdriver.common.by import By
from conftest import browser_with_login, handle_fail, error_file_path

def test_case_1_1(browser_with_login, error_file_path):
    with handle_fail(browser_with_login, error_file_path):
        selected_text = browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]/div/div[1]/div[2]').text
        specified_text = "Free Trials"
        assert selected_text == specified_text

def test_case_1_2(browser_with_login, error_file_path):
    with handle_fail(browser_with_login, error_file_path):
        selected_text = browser_with_login.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[3]/div[2]/div/div[1]/div[2]').text
        specified_text = "Free Trial"
        assert selected_text == specified_text        

