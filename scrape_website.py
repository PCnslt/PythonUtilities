from bs4 import BeautifulSoup
import requests

def get_currency_rate(in_curr, out_curr):
    """Use beautiful soup to scape data from FE url"""
    url = f'https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1'
    content = requests.get(url, timeout=120).text
    #BeautifulSoup
    soup= BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(rate[:-4])
    return rate

print(get_currency_rate('USD', 'EUR'))
