#-*- coding: utf-8 -*-
"""
Webscrape text of the Australian news website www.abc.net.au/news
@author: roelientimmer
"""

from bs4 import BeautifulSoup
import requests
import winsound

URL_start = 'https://www.abc.net.au/news/'

f = open("news.txt", "x") #create a new txt file

history=100000  #number of links you want to check
                #important note: a lot of links will be empty 

count=0 #the number of articles found

for i in range((12248344-history),12248345):
    
    URL = URL_start+str(i) 
    page=requests.get(URL)
    soup=BeautifulSoup(page.content, 'html.parser')
    
    items=soup.find_all('p', class_='_1SzQc')
    
    if items:
        f.write('\n \n') #skip two lines
        count=count+1 #the number of articles found
    
    for item in items:
        try:
            f.write(item.text)
            f.write('\n')
        except:
            winsound.Beep(2500,1000) #beep noise to notify that writing went wrong
            
f.close() #close txt file
  
print('Total number of news articles found: ', count)
winsound.Beep(2000, 1000) #beep noise to notify that the script is finished      