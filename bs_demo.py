import requests
from bs4 import BeautifulSoup as bs

username = input('Please enter github username: ')

url = "https://github.com/" + username

response = requests.get(url)

soup = bs(response.content, "html.parser")

profile_img = soup.find('img', {'alt' : 'Avatar'})['src']

print(profile_img)

