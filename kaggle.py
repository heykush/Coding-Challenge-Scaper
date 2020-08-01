import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")
url="https://www.kaggle.com/competitions"
r = requests.get(url)
driver.get(url)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
liv=[]
ksite=driver.find_elements_by_xpath('//*[@class="sc-qamJO dNzqXp mdc-list sc-qYGzz cjQBWh mdc-list--avatar-list mdc-list--three-line"]')
print("\n==================== LIVE CHALLENGE ==========\n ")
sleep(2)
for i in ksite:
	lin=i.find_elements_by_tag_name('li')
	liv.extend(lin)

for j in liv:
	print("\n=======================\n", j.text , end="\n")
