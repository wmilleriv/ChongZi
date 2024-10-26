import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#r=requests.get('http://www.baobao88.com/list/21/4--0--155--.html')

#soup=BeautifulSoup(r.content,'html.parser')
driver=webdriver.Firefox()
driver.get('http://www.baobao88.com/list/21/4--0--155--.hml')

links = driver.find_elements(By.CLASSNAME, "tip")

for link in link:
    link.click()
    stories.append(driver.find_element_by_id("tuimg"))

#for story in stories
print(stories)

#s=soup.find('div', class_='list_right_nr1')
#for link in s.find_all('a'):
    #print(link.get('href'))



