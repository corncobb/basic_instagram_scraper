#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json

class InstagramScraper:

    def __init__(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

    def getinfo(self, url): #this function will get the username, followers, and following
        try:
            html = urllib.request.urlopen(url, context=self.ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            data = soup.find_all('meta', attrs={'property': 'og:description'
                                 })
            text = data[0].get('content').split()
            user = text[-1]
            followers = text[0]
            following = text[2]
            print(user + ' ' + 'Following: ' + following + ' Followers: ' + followers)
        
        except:
            print("Failed to get info for " + url)

    #More methods can be added but are not necessary for current needs

def main():
    obj = InstagramScraper()
    username_list = []
    print("Enter/Paste elements, press[Enter], then press Ctrl-D to save it and run program.")

    while(True):
        
        try:
            user = input()
          
        except EOFError:
            break
        
        for x in user.split():
            username_list.append(x)

    #used only if wanting to enter by url instead of username
    '''
    with open('users.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in self.content]
    for url in self.content:
        getfollowings(url)
    '''
    for x in username_list:
        obj.getinfo('https://www.instagram.com/{}/'.format(x))

if __name__ == '__main__':
    main()
