from bs4 import BeautifulSoup
from selenium import webdriver

driver =webdriver.Chrome('C:/Users\swphe\Downloads\chromedriver')
driver.get("https://nid.naver.com/nidlogin.login")

driver.find_element_by_name('id').send_keys('ID')
driver.find_element_by_name('pw').send_keys('PW')

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

driver.get('https://order.pay.naver.com/home') # Naver 페이 들어가기
html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())