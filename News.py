import requests
from bs4 import BeautifulSoup

url = 'https://www.bleepingcomputer.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
titles = soup.find_all('h4', limit=10)
for title in titles:
    print(title.get_text())
