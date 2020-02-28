import pandas as pd
import requests as r
from bs4 import BeautifulSoup

page='https://www.yelp.com/biz/amami-sushi-bistro-san-francisco-2'
request=r.get(page)
soup=BeautifulSoup(request.text,"html.parser")


post=soup.find_all('li',{'class':'lemon--li__373c0__1r9wz u-space-b3 u-padding-b3 border--bottom__373c0__uPbXS border-color--default__373c0__2oFDT'})
#nome=post.find_all('a', {'class':'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--default__373c0__1skgq'})



for posts in post:
    nome=([nomes.text for nomes in posts.find_all('span', {'class':'lemon--span__373c0__3997G text__373c0__2pB8f fs-block text-color--inherit__373c0__w_15m text-align--left__373c0__2pnx_ text-weight--bold__373c0__3HYJa'})])
    coment=([coments.text for coments in posts.find_all('p', {'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f comment__373c0__3EKjH text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_'})])
    date=([dates.text for dates in posts.find_all('span',{'class':'lemon--span__373c0__3997G text__373c0__2pB8f text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_'})])
    print(nome,date,coment)
