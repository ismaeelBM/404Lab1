import requests

print(requests.__version__)

google_get = requests.get('https://www.google.com')

git_get = requests.get('https://raw.githubusercontent.com/ismaeelBM/404Lab1/master/requests_version.py')

print(git_get.text)