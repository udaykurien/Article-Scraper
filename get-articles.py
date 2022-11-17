import cloudscraper
from bs4 import BeautifulSoup

menu = '# Journal options:\n\
# 0. Quit\n\
# 1. New York Times\n\
# 2. The Economist\n\
# 3. New Yorker'

print(menu)

repeat = True
while repeat:
  repeat = False
  jrnl_optn = int(input("Enter journal option: "))
  if jrnl_optn == 1:
    attributes = {'class':'css-at9mc1 evys1bk0'}
  elif jrnl_optn == 2:
    attributes = {'class':'article__body-text'}
  elif jrnl_optn == 3:
    attributes = {'class':'paywall'}
  elif jrnl_optn ==0:
    quit()
  else:
    print("Invalid selection")
    repeat = True

url = input("Enter article url: ")

fname = url.split('/')[-1].split('.html')[0]
floc = 'Articles'
fpath = floc + '/' + fname


scraper = cloudscraper.create_scraper()
response = scraper.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
para = soup.find_all(attrs=attributes)

with open(fpath, 'w') as f:
  for line in para:
    f.write(line.text)
    f.write("\n")


#url = 'https://www.nytimes.com/2022/10/26/opinion/grief-death-lessons-on-living.html'
#url = 'https://www.economist.com/graphic-detail/2022/11/14/a-rare-reason-for-optimism-about-climate-change'
