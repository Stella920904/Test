from Modules import *

def get_chrome_driver():
    return webdriver.Chrome(ChromeDriverManager().install())