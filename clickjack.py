import requests

#domain = 'https://www.hackthissite.org/'
domain = 'https://www.google.com/'
headers = requests.get(domain).headers

if 'X-Frame-Options' in headers:
    print(domain + ' is NOT VULNERABLE')
else:
    print(domain + ' is VULNERABLE')

