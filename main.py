from bs4 import BeautifulSoup
import requests


response = requests.get("https://finance.i.ua/nbu/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text,features="html.parser")
    dolar_list = soup.find_all("span", {"value"})
    euro_list = soup.find_all("span", {"value"})
    rez = dolar_list[0].find("span")
    rez1 = euro_list[1].find("span")
    print(rez.text)
    print(rez1.text)
