import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")
url= "https://www.hackerearth.com/challenges/"
r = requests.get(url)
driver.get(url)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
live=driver.find_elements_by_xpath('//*[@class="ongoing challenge-list"]')
upcoming=driver.find_elements_by_xpath('//*[@class="upcoming challenge-list"]')

liv=[]
liv2=[]

for k in live:
	lin=k.find_elements_by_class_name('challenge-card-modern')
	liv.extend(lin)

for l in liv:
	b=print("\n=======================\n", l.text , end="\n")
	# print(b)
for i in upcoming:
	lin2=i.find_elements_by_class_name('challenge-card-modern')
	liv2.extend(lin2)

for j in liv2:
	c=print("\n=======================\n", j.text , end="\n")
	# print(c)

# To print in excel file
df= pd.DataFrame({
"Live": b,
"Upcoming":c,},index=[0])
df.to_excel("hacker.xlsx")

# ,index=False,header=True