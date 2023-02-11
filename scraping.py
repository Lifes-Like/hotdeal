import requests
import re
import time
import pyshorteners
from bs4 import BeautifulSoup

headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
s = pyshorteners.Shortener()
source = 'https://www.fmkorea.com'
url = f'{source}/index.php?mid=hotdeal&sort_index=pop&order_type=desc&page=1'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
deals = soup.find_all('li', attrs={'class':re.compile('hotdeal0$')})

for deal in deals:
    title = re.sub(r'\[[0-9]{1,4}\]','',deal.find('h3', attrs={'class':'title'}).get_text())
    if '포텐' in title:
        title = title.replace('포텐','')
    else:
        continue
    deal_info = deal.find_all('a', attrs={'class':'strong'})
    # link = deal.find_all('a', attrs={'class':'strong'})[0]['href']
    # price = deal.find_all('a', attrs={'class':'strong'})[1].get_text()
    # delivery = deal.find_all('a', attrs={'class':'strong'})[2].get_text()
    print(f'''{title.strip()}, 가격 : {deal_info[1].get_text()}, 배송 : {deal_info[2].get_text()}, 링크 : {s.tinyurl.short(source + deal_info[0]['href'])}''')
    time.sleep(3)