import csv

import requests
from bs4 import BeautifulSoup
import re
from fbchat import Client
from fbchat.models import *



def findpid(url):
    """ Function that recive a url of facebook page and
    find his id using the web: findmyfbid.com.
    Parameters:
        `url`: string type, url to find.
        return: string type, id of face page. """

    # setting headers and url to open
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'url':url}
    baseurl="https://findmyfbid.com/"
    session = requests.Session()
    response=session.post(baseurl, headers=headers, data=payload)

    # set up beautifulsoup to find de id in the url response
    soup=BeautifulSoup(response.text,"html.parser")
    #code = soup.find_all('code').getText()
    #print(response.text)#debug
    # find the code tag, get text and finally return it
    #code = soup.code.getText()
    return response.text
    #print(code)#debug


if __name__ == "__main__":
    client = Client('lbenbary@gmail.com', 'vall1234!')
    with open('tst.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            #print(row)
            us=findpid(row)
            id=re.findall('\d+', us)
            #print(id)
            #client.send(Message(text='Hi me!'), thread_id=id, thread_type=ThreadType.USER)
            client.sendLocalImage('/home/med/Pictures/dmaccees.png', message=Message(text='chov 4ak!'), thread_id=id, thread_type=ThreadType.USER)
    client.logout()


