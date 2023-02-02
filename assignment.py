import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {'User_Agent': 'Mozilla/5.0 (windows NT 10; Win64; rv:94.0; Gecko/20100101 Firefox/94.0',
          'Accept-Language': 'en-US, en;q=0.5'}

product_name = []
product_url = []
product_price = []
product_rating = []

for i in range(20):
    url = f"https://www.amazon.in/s?k=bags&page={i+1}&crid=TM81KO1HTH2K&qid=1675267432&sprefix=bag%2Caps%2C221&ref=sr_pg_2"
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    result = soup.find_all('div', class_='sg-col-inner')
    for re in result:
        product = re.find('div', class_='a-section a-spacing-none puis-padding-right-small s-title-instructions-style')
        price = re.find('span', class_='a-price-whole')
        rating = re.find('span', class_='a-size-base s-underline-text')
        
        try:
            product_name.append(product.h2.a.span.text)
            product_url.append('https://www.amazon.in/'+product.h2.a.get('href'))
            product_price.append(price.text+'rs.')
            product_rating.append(rating.text)
            print(rating.text)
        except AttributeError:
            continue

data = {'Product': product_name, 'Price': product_price,
        'Rating': product_rating, 'Url': product_url}
df = pd.DataFrame.from_dict(data, orient='index').T
df.to_csv('data1.csv',index=False)