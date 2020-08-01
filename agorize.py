import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")
url="https://www.agorize.com/en/challenges?group"
r = requests.get(url)
driver.get(url)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
sleep(2)

ksite=driver.find_elements_by_xpath('//*[@class="challengeCardsList d-flex flex-wrap"]')
liv=[]

for i in ksite:
	lin=i.find_elements_by_class_name('challengeCard')
	liv.extend(lin)

for j in liv:
	print("\n=======================\n", j.text , end="\n")






















