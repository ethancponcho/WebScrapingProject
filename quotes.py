from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

page_num = 1
webpage = 'https://quotes.toscrape.com/page/' + str(page_num)
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
page = urlopen(webpage)
soup = BeautifulSoup(page, 'html.parser')

print(soup.title.text)
quotes_section = soup.findAll('div', class_='quote')

author_count = {}
tag_count = {}
longest_length = 0
shortest_length = 0
longest_quote = ()
shortest_quote = ()
total_length = 0


for quote in quotes_section:
    quote_text = quote.find('span', class_='').text
    author = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]
    
    if author in author_count:
        author_count[author] += 1
        
    quote_length = len(quote_text)
    total_length += quote_length
    
    if quote_length > longest_length:
        longest_length = quote_length
        longest_quote = quote_text
    if quote_length < shortest_length:
        shortest_length = quote_length
        shortest_quote = quote_text
        
    for tag in tags:
        tag_count[tag] += 1

average_length = total_length / len(quotes_section)    
most_quotes = max(author_count, key=author_count.get)
least_quotes = min(author_count, key=author_count.get)
popular_tag = max(tag_count, key=tag_count.get)
total_tag = sum(tag_count.values())

print(f"Author with Most Quotes: {most_quotes}")
print(f"Author with Least Quotes: {least_quotes}")
print(f"Average Length of Quotes: {average_length}")
print(f"Longest Quote: {longest_quote}")
print(f"Shortest Quote: {shortest_quote}")
print(f"Most Popular Tag: {popular_tag}")
print(f"Total Tags Among Quotes: {total_tag}")
print(f"")