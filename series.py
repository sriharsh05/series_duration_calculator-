#series duration calculator with webscraping
import requests
from bs4 import BeautifulSoup
import re

series="how i met your mother"
series=series.title()
series = series.replace(" ","_")  #URLs of wikipedia contains '_' in the place of " "

url_init = "https://en.wikipedia.org/wiki/"
url=url_init+series+"_(TV_series)"  
# print(url)

r = requests.get(url)
soup = BeautifulSoup(r.content	, 'html.parser')


thead = soup.find_all('th',class_='infobox-label')     #returns all the elements of table head
tdata = soup.find_all('td',class_='infobox-data')      #returns all the elements of table data

count_episodes=0
for i in thead:                              #looping and incrementing the count until we get "No of episodes" in table head
    if i.get_text()=="No. of episodes":
        break
    count_episodes+=1


count_rtime=0
for i in thead:                            #looping and incrementing the count until we get "running time" in table head
    if i.get_text()=="Running time":
        break
    count_rtime+=1 

try:
    rtime=tdata[count_rtime].get_text()              #accessing episodes using count
    episodes =tdata[count_episodes].get_text()       #accessing time using count
    numbers_episodes=re.findall('\d+',episodes)      #using regular expressions to extract numbers from strings
    numbers_runtime=re.findall('\d+',rtime)
    if len(numbers_runtime)>1 :
            duration=((int(numbers_runtime[0])+int(numbers_runtime[1]))/2)*int(numbers_episodes[0])
    else :  
            duration=(int(numbers_runtime[0]))*int(numbers_episodes[0])
    print("Number of episodes :",episodes)      
    print("Running Time :",rtime)              
    print("Approximate duration :",duration," minutes")

except:
    url=url_init+series                        #repeating everything again without appending "_TV(Series)" to the url
    r = requests.get(url)
    # print(url)
    soup = BeautifulSoup(r.content	, 'html.parser')
    

    thead = soup.find_all('th',class_='infobox-label')
    tdata = soup.find_all('td',class_='infobox-data')
    
    count_episodes=0
    for i in thead:
        if i.get_text()=="No. of episodes":
            break
        count_episodes+=1


    count_rtime=0
    for i in thead:
        if i.get_text()=="Running time":
            break
        count_rtime+=1 

    try:
        rtime=tdata[count_rtime].get_text()              #accessing episodes using count
        episodes =tdata[count_episodes].get_text()       #accessing time using count
        numbers_episodes=re.findall('\d+',episodes)      #using regular expressions to extract numbers from strings
        numbers_runtime=re.findall('\d+',rtime) 
        if len(numbers_runtime)>1 :
            duration=((int(numbers_runtime[0])+int(numbers_runtime[1]))/2)*int(numbers_episodes[0])
        else :  
            duration=(int(numbers_runtime[0]))*int(numbers_episodes[0])
  
        
        print("Number of episodes :",episodes)      
        print("Running Time :",rtime)              
        print("Approximate duration :",duration," minutes")   
    except:
        print("No series")     

