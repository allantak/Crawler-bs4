import requests
from bs4 import BeautifulSoup

requi=requests.get('https://br.advfn.com/indicadores/taxa-selic/valores-historicos')

soup=BeautifulSoup(requi.content,"html.parser")


geral=soup.find('div', id='section_1')
inf= geral.find_all('td')

for infos in inf:
    print(infos.text)

    








