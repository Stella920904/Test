import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    # options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=options)
    yield driver
    
    driver.quit()
