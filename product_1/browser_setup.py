import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def browser():
    # options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install())
    yield driver


    driver.quit()
