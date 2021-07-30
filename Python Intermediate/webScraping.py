from typing import Text
import requests
from bs4 import BeautifulSoup
url='https://docs.google.com/forms/d/e/1FAIpQLSc3Xc_3a5U8FNnazzpkpEOWTQtUFoUJq1ejpbe_mAqFa2-1Yw/formResponse'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
# print(soup)
quotes=soup.find_all('div',class_='freebirdFormviewerViewItemsEmbeddedobjectLeft')
# authors= soup.find_all('small',class_='author')
# tags=soup.find_all('div',class_='tags')
for i in range(0, len(quotes)):
    print(quotes[i].text)
    # print(authors[i].text)
    # quoteTags=tags[i].find_all('a',class_='tag')
    # for quoteTag in quoteTags:
        # print(quoteTag.text)
# print(authors)
