import requests
import re
from bs4 import BeautifulSoup

url = 'https://github.com/{}'
username = "NimaXploit"

r = requests.get(url.format(username), params={'tab':'repositories'})
content = BeautifulSoup(r.text , 'html.parser')
repos_element = content.find(id='user-repositories-list')
repos = repos_element.find_all('li')
for repo in repos:
    name = repo.find('h3').find('a').get_text(strip=True)
    language = repo.find(attrs={'itemprop':'programmingLanguage'})
    language = language.get_text(strip=True) if language else 'unknown'
    stars = repo.find('a', attrs={'href':re.compile('\/stargazers')})
    stars = int(stars.get_text(strip=True)) if stars else '0'
    print(name, language, stars)
    