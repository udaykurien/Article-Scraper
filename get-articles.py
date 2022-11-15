import cloudscraper
from bs4 import BeautifulSoup

# Journal options:
# 1. New York Times
# 2. The Economist

jrnl_optn = 3

url = 'https://www.nytimes.com/2022/10/26/opinion/grief-death-lessons-on-living.html'
url = 'https://www.economist.com/graphic-detail/2022/11/14/a-rare-reason-for-optimism-about-climate-change'

fname = url.split('/')[-1].split('.html')[0]
floc = 'Articles'
fpath = floc + '/' + fname

if jrnl_optn == 1:
  attributes = {'class':'css-at9mc1 evys1bk0'}
elif jrnl_optn == 2:
  attributes = {'class': 'article__body-text'}
else:
  print("Invalid selection")
  quit()

scraper = cloudscraper.create_scraper()
response = scraper.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
para = soup.find_all(attrs=attributes)

with open(fpath, 'w') as f:
  for line in para:
    f.write(line.text)
    f.write("\n")


