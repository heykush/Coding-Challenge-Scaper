import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")
url="https://challengerocket.com/hackathons-and-challenges.html"
r = requests.get(url)
driver.get(url)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
sleep(2)
print("\n==================== LIVE CHALLENGE ==========\n ")
condition=True
while condition:
	liv=[]
	ksite=driver.find_elements_by_xpath('//*[@class="list"]')
	for i in ksite:
		lin=i.find_elements_by_tag_name('li')
		liv.extend(lin)

	for j in liv:
		print("\n=======================\n", j.text , end="\n")

	try:	
		sleep(3)
		nex=driver.find_elements_by_xpath('//*[@id="all"]/section/div/div[2]/ul/li[6]/a').click()
		sleep(4) 
	except:
		condition=False