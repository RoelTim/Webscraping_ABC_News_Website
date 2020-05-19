from bs4 import BeautifulSoup
import requests
import winsound

URL_start = 'https://www.abc.net.au/news/'

f = open("news.txt", "a+") #append

history=100000  #number of links you want to check
                #important note: a lot of links will be empty 
"""
Webscrape text of the Australian news website www.abc.net.au/news
@author: roelientimmer
"""

count=2382 #the number of articles found

for i in range((12210593-history),12248345):
    try:
        URL = URL_start+str(i) 
        page=requests.get(URL)
        soup=BeautifulSoup(page.content, 'html.parser')
        items=soup.find_all('p', class_='_1SzQc')
        if items:
            f.write('\n \n') #skip two lines
            count=count+1 #the number of articles found
        try:
            for item in items:   
                f.write(item.text)
                f.write('\n')
        except:
            winsound.Beep(2500,1000) #beep noise to notify that writing went wrong
            print('Something with text writing went wrong.')
            print('See article nr.: ',i)
    except:
        winsound.Beep(2500,1000) #beep noise to notify that writing went wrong
        print('Something with beautifulsoup went wrong.')
        print('See article nr.: ',i)
            
f.close() #close txt file
  
print('Total number of news articles found: ', count)
winsound.Beep(2000, 1000) #beep noise to notify that the script is finished      
