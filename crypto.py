from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.slickcharts.com/currency'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text)
print()


crypto_data = soup.find("table",attrs={"class":"table table-hover"}).find('tbody').findAll('td')
    
counter = 0

for x in range(5):
    name = crypto_data[counter+1].text
    curr_price = float(crypto_data[counter + 5].text.strip('$').replace(',', '').split('\n')[0])
    perc_change = float(crypto_data[counter + 6].text.strip('%').split('\n')[0])
    corres_price = curr_price * perc_change
    
    print(f"Cryptocurrency Name:{name}")
    print(f"Current Price: ${curr_price:.2f}")
    print(f"Percentage Change: {perc_change:.2f}%")
    print(f"Corresponding Price (Based on Change in Percentage): ${corres_price:.2f}")
    print()
    print()
    counter += 6