from bs4 import BeautifulSoup 
import requests

response = requests.get('https://fr.wikipedia.org/wiki/Alger')
#print(response.status_code)

#print(response.headers)

#print(response.text)
#***************************************
soup = BeautifulSoup(response.text , 'html.parser')

tables = soup.find('table')
pop = tables.find_all('tr')[14].td.text
print(pop)




