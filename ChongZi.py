import requests
from bs4 import BeautifulSoup

r=requests.get('http://www.baobao88.com/list/21/4--0--155--.html')

print(r)
soup=BeautifulSoup(r.content,'html.parser')
print(soup.prettify())

s=soup.find('div', class_='list_right_nr1')
for link in s.find_all('a'):
    print(link.get('href'))



