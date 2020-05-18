# Webscraping_ABC_News_Website
Webscraping articles of https://www.abc.net.au/news/ with Python.

![Banner abc news](https://github.com/RoelTim/Webscraping_ABC_News_Website/blob/master/ABC_news_banner.PNG)

Remarks:
- The texts of the articles will be saved in news.txt
- With the variable 'history' you can select how many links you want to check. Every link contains at most one news article and some are empty.
- The code will be changed such that you can download all the ABC news articles including the most recent ones.

First import the relevant packages. If you do not have them on your pc yet you can download them.
```python
from bs4 import BeautifulSoup #if not existing --> pip install beautifulsoup
import requests #if not existing --> pip install requests
import winsound #if not windsound --> pip install windsound
```
Open a txt file to write all the news articles in.
```python
f = open("news.txt", "x") #create a new txt file
```
Define the abc.new.au URL, set the number of links you want to check for articles.
```python
URL_start = 'https://www.abc.net.au/news/'
history=100000  #number of links you want to check
                #important note: a lot of links will be empty 
```
We will count how many articles we will find. Some of the links will be empty and will therefore not add to the total number of articles.
```python
count=0 #the number of articles found
```
With a loop we webscrape all the different webpages.
```python
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
```
Save and close the txt file, show the number of articles we found and end with a beeping sound. 
The beeping sounds is added as an alert. As the running time of this script can be very long it is handy to have an alert ones the script is ready
```python
f.close() #close txt file
print('Total number of news articles found: ', count)
winsound.Beep(2000, 1000) #beep noise to notify that the script is finished      
```
