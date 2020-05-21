import requests
from bs4 import BeautifulSoup

url = 'https://cbr.ru/'
try:
    source = requests.get(url)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

main_text = source.text
# print(main_text)
soup = BeautifulSoup (main_text, features="html.parser")
dollar = soup.find_all('div', {"class":"indicator_el_value mono-num"})

# print(dollar)
lst = [baks.parent.get_text() for baks in dollar]
# print(lst)
print('Курс доллара сегодня: '.rjust(22,' ')+lst[1][1:-1])
print('Курс доллара вчера: '.rjust(22,' ')+lst[0][1:-1])
print('Курс евро сегодня: '.rjust(22,' ')+lst[3][1:-1])
print('Курс евро вчера: '.rjust(22,' ')+lst[2][1:-1])
