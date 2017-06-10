from bs4 import BeautifulSoup

soup = BeautifulSoup(open('index.html'), "lxml")
for tag in soup():
  for attribute in ['class','style', 'id', 'style']:
    del tag[attribute]
    print tag+"\n"

