import requests

from bs4 import BeautifulSoup

proxy_Domain = ("https://www.proxynova.com/proxy-server-list/", "tbl_proxy_list")

r = requests.get(proxy_Domain[0])

soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find('table', {'id': proxy_Domain[1]})

for row in table.find_all('tr'):
        columns = row.find_all('td')
        try:
            print('-------')
            print('%s:%s%-10s%-10s' % (columns[0].find('abbr').attrs['title'],
                                       columns[1].get_text(),
                                       columns[5].get_text(),
                                       columns[6].get_text()
                                       )
                  )
        except:
            pass







