import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")
url="https://www.techgig.com/challenge"
r = requests.get(url)
driver.get(url)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
sleep(2)

ksite=driver.find_elements_by_xpath('//*[@class="contest-listing"]')
liv=[]

for i in ksite:
	lin=i.find_elements_by_xpath('//*[@class="contest-box prize-hiring-1"]')
	liv.extend(lin)
	lin1=i.find_elements_by_xpath('//*[@class="contest-box prize-hiring-2"]')
	liv.extend(lin1)
for j in liv:
	print("\n=======================\n", j.text , end="\n")


