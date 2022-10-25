from bs4 import BeautifulSoup
import lxml

with open ('home.html') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

print(soup.a)

all_anchor_tags = soup.find_all(name="a")

print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get('href'))

# returns list
heading = soup.find_all(name = 'h1', id='name')

print(heading)

heading_3 = soup.find(name = 'h3', class_='heading')

print(heading_3)

company_url = soup.select_one(selector='p a')

print(company_url)

company_url_a = soup.select_one(selector='#name')

print(company_url_a)

company_url_b = soup.select(selector='.heading')

print(company_url_b)


