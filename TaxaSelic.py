import requests
from bs4 import BeautifulSoup
import csv

f=open('taxaSelic.csv','w',newline='')
write=csv.writer(f)
requi=requests.get('https://br.advfn.com/indicadores/taxa-selic/valores-historicos')

soup=BeautifulSoup(requi.content,"html.parser")


geral=soup('div', id='section_1')[0].find_all('tr')
#inf= geral.find_all('td')

for infos in geral:
        cols=infos.findChildren(recursive=False)
        cols=[ele.text.strip() for ele in cols]
        write.writerow(cols)
        print(cols)


   



    








