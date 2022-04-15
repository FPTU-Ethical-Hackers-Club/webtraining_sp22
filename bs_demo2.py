import requests
from bs4 import BeautifulSoup as bs

username = input('Please enter github username: ')

url = "https://github.com/" + username + "?tab=repositories"

response = requests.get(url)

soup = bs(response.content, "html.parser")

repos = soup.find_all('a', {'itemprop' : 'name codeRepository'})

for repo in repos:
    print("Ten: " + repo.text)
    print("\nURL: " + "https://github.com/" + repo['href'])