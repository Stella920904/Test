from Modules import *
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
def get_chrome_driver():
    return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)