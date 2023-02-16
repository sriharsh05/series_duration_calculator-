#Series duration calculator with webscraping and TKinter
import tkinter as tk
from bs4 import BeautifulSoup
import requests
import re

def scrape_website():
    
    series = series_entry.get()
    series=series.title()
    series = series.replace(" ","_")  #URLs of wikipedia contains '_' in the place of " "

    url_init = "https://en.wikipedia.org/wiki/"
    url=url_init+series+"_(TV_series)"  
        
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
            
        results_label1.config(text="Number of episodes: "+episodes)
        results_label2.config(text="Running Time: "+ rtime)
        results_label3.config(text="Duration: "+str(duration)+" minutes")
    except:
        url=url_init+series                        #repeating everything again without appending "_TV(Series)" to the url
        r = requests.get(url)
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
                
            results_label1.config(text="Number of episodes: "+episodes)
            results_label2.config(text="Running Time: "+ rtime)
            results_label3.config(text="Duration: "+str(duration)+" minutes")
        
        except:
            results_label1.config(text="Invalid")
            results_label2.config(text="")
            results_label3.config(text="")
        

root = tk.Tk()   # Creating a Tkinter window
root.title("Series Duration Calculator")

series_label = tk.Label(root, text="Enter the series:")   # Creating a label for the URL input
series_label.pack()

# Creating an entry field for the URL
series_entry = tk.Entry(root)
series_entry.pack()

# Creating a button to scrape the website
scrape_button = tk.Button(root, text="Find",bg="black", fg="white", command=scrape_website)
scrape_button.pack()

# Creating  labels for the results
results_label1 = tk.Label(root, text="")
results_label1.pack()

results_label2 = tk.Label(root, text="")
results_label2.pack()

results_label3 = tk.Label(root, text="")
results_label3.pack()

# Run the Tkinter mainloop
root.mainloop()
