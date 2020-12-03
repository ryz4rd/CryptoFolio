import requests
from bs4 import BeautifulSoup

url = 'https://www.coingecko.com/es'

soup = BeautifulSoup(requests.get(url).content, 'html.parser')
soup_prices = BeautifulSoup(requests.get(url).content, 'html.parser')
# VARIABLES
nameCrypto = []
prices = []
old_prices = [] # NO SE USA
old_names = [] # NO SE USA

#OBTENER NOMBRES PERO SIN FORMATEAR
for name in soup.find_all('a', attrs={"class":"d-lg-none font-bold"}):
    old_names.append(name.text)

#NOMBRES FORMATEADOS
for names in old_names:
    nameCrypto.append(names.strip())

#PRECIOS SIN FORMATEAR
for price in soup_prices.find_all('td', attrs={"class":"td-price price text-right"}):
    old_prices.append(price.text)

# PRECIOS FORMATEADOS    
for price in old_prices:
    prices.append(price.strip())


# CREACION DEL DICCIONARIO    
cryptoVal = zip(nameCrypto, prices)
cryptoVal = dict(cryptoVal)

user_token = input("CRIPTOMONEDA: ")
user_token = user_token.upper()
user_value = cryptoVal[user_token]
print(f'El precio actual de {user_token} es de: {user_value}')
