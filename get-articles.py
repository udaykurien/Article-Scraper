import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

df=pd.read_csv('jrnl_class_lst.csv')
df_sorted=df.sort_values(by='Journal').reset_index(drop=True)
df_sorted.index += 1

menu=df_sorted['Journal'].to_string()
menu = "0    Quit\n" + menu
print(menu)

repeat = True
while repeat:
  repeat = False
  jrnl_optn = int(input("Enter journal option: ")) -1
  if jrnl_optn == -1:
    quit()
  elif jrnl_optn >=0 and jrnl_optn <= df_sorted.shape[0] - 1:
    print(df_sorted.iloc[jrnl_optn,1])
    attributes = {'class':df_sorted.iloc[jrnl_optn,1]}
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