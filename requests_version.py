import requests

print(requests.__version__)

google_get = requests.get('https://www.google.com')
print(google_get.status_code)