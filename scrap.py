import requests
from bs4 import BeautifulSoup as BS
import sys

url = "https://upsc.gov.in/examinations/previous-question-papers"
response = requests.get(url)
if response.status_code == 200:
    webpage_content= response.text
else:
    print("failed to find page")
    sys.exit()

soup = BS(webpage_content,'html.parser')
links = soup.find_all('span', class_="file")

for link in links:
    print(link.a['href'])
input()