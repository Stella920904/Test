import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹드라이버를 설정합니다.
driver = webdriver.Chrome()  # 또는 webdriver.Chrome(), webdriver.Safari() 등

# 웹페이지를 불러옵니다.
driver.get("https://qa.surffy-dev.io/ko/product/netfunnel/")  # 텍스트를 검증하고 싶은 웹페이지 URL

# 웹페이지에서 텍스트를 가져옵니다. 아래 예시는 웹페이지의 body 전체 텍스트를 가져옵니다.
page_text = driver.find_element(By.TAG_NAME, 'body')
print(page_text)

# 엑셀 파일을 불러옵니다.
df = pd.read_excel('STCLab Localization.xlsx', engine='openpyxl')

# 'A1' 셀의 값을 가져옵니다.
cell_value = df.iat[0, 9]  # 'A1' 셀은 index로는 [0, 0]에 해당합니다.
print(cell_value)


# 웹페이지의 텍스트와 엑셀의 셀값을 비교합니다.
if cell_value == page_text:
    print("The texts are identical.")
else:
    print("The texts are not identical.")

# 웹드라이버를 종료합니다.
driver.quit()