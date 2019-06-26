import requests

r = requests.get('http://example.com/')
print(r.text)

print('-------------------------------------------------')
url = 'http://example.com/'
par = {'Key1': 'value1', 'Key2': 'value2'}
r = requests.get(url, params=par)
print(r.url)

print('-------------------------------------------------')
url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, params=cookies)
print(r.text)
print(r.cookies['example_cookie_name'])