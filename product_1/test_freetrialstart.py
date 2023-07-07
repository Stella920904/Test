import pytest
from selenium.webdriver.common.by import By
from conftest import browser_with_surffymain, handle_fail, error_file_path

def test_case_1_1(browser_with_surffymain, error_file_path):
    with handle_fail(browser_with_surffymain, error_file_path):
        selected_text = browser_with_surffymain.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/h3').text
        specified_text = "NetFUNNEL"
        assert selected_text == specified_text

def test_case_1_2(browser_with_surffymain, error_file_path):
    with handle_fail(browser_with_surffymain, error_file_path):
        selected_text = browser_with_surffymain.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/div[2]/div').text
        specified_text = "작동중"
        assert selected_text == specified_text