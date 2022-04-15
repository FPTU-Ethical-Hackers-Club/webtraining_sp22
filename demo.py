import requests, json
from getpass import getpass

url = "https://damcode2.herokuapp.com/controller/authentication.php"

data = {
    'username' : 'teacher',
    'password' : '123'
}

response = requests.post(url, data=data, timeout=(1,2), follow_redirect=false)

print(response.content)