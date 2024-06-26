import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

rand_chapters=random.randrange(1,22)
if rand_chapters < 10:
    rand_chapters = '0' + str(rand_chapters)
else:
    rand_chapters = str(rand_chapters)
    
webpage ='https://ebible.org/asv/JHN' + rand_chapters + '.htm'
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
page = urlopen(webpage)
soup = BeautifulSoup(page, 'html.parser')

print(soup.title.text)

chapter_verses_list = []

#chapter_verses = soup.findAll("div",attrs={"class":"p"})
pages_verses = soup.findAll('div', class_='p')

for section_verse in pages_verses:
    verse_list = section_verse.text.split('.')
    for v in verse_list:
        chapter_verses_list.append(v)

my_verses = [i for i in chapter_verses_list if i != ' ']
chosen_verse = random.choice(my_verses)

print(f"Chapter: {rand_chapters}, Verse:{chosen_verse}")