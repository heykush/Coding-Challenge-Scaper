import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")
url="https://www.bemyapp.com/events/"
r = requests.get(url)
driver.get(url)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
sleep(2)
# print("\nx==================== LIVE CHALLENGE ==========\n ")
condition=True
while condition:
	liv=[]
	ksite=driver.find_elements_by_xpath('/html/body/section[2]/div/div/div[2]')
	for i in ksite:
		lin=i.find_elements_by_class_name('events-card')
		liv.extend(lin)

	for j in liv:
		print("\n=======================\n", j.text , end="\n")
	try:
		sleep(3)
		nex=driver.find_element_by_xpath('/html/body/section[2]/div/div/div[3]/div/ul/li[7]/a').click()
		sleep(4) 
	except:
		condition=False