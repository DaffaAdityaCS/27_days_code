import re
import requests
import urllib.request


def donwload():
    #take a link from user
    link = input(str("insert URL:"))

    #read html data 
    html = requests.get(link)

    #parse URL
    try:
        url = re.search('hd_src:"(.+?)"', html.text) [1]
        print("HD Video")
    except:
        url = re.search('sd_src:"(.+?)"' ,html.text) [1]    
        print("SD Video")

    inpt = input(str("video Name: "))
    name = inpt + str(".mp4")
    
    print("Donwloading..")
    urllib.request.urlretrieve(url, name)
    print("Donwload Done")


donwload()
