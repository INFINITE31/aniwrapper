import requests
from random import choice
import json


base_url = "https://anime-api.hisoka17.repl.co/img"
endpoints = ["slap","kiss","cuddle","hug","kill","wink","pat"]

class anime():
    def __init__(self):
        super().__init__()

    def kiss(link:bool):
        r = requests.get(f"{base_url}/kiss")

        if link == True:
            link = r.json()["url"]
            return link
        if link == False:

            link = r.json()["url"]
            content = requests.get(link).content
            return content

    def slap(link:bool):
        r = requests.get(base_url+"/slap")

        if link == True:
            link = r.json()["url"]
            return link
        if link == False:
            link = r.json()["url"]
            content = requests.get(link).content
            return content

    def kill(link:bool):
        r = requests.get(base_url+"/kill")

        if link == True:
            link = r.json()["url"]
            return link
        if link == False:
            link = r.json()["url"]
            content = requests.get(link).content
            return content

    def hug(link:bool):
        r = requests.get(base_url+"/hug")

        if link == True:
            link = r.json()["url"]
            return link
        if link == False:
            link = r.json()["url"]
            content = requests.get(link).content
            return content

    def wink(link:bool):
        r = requests.get(base_url+"/wink")

        if link == True:
            link = r.json()["url"]
            return link
        if link == False:
            link = r.json()["url"]
            content = requests.get(link).content
            return content

    def pat(link:bool):
        r = requests.get(base_url+"/pat")

        if link == True:
            link = r.json()["url"]
            return link
        if link == False:
            link = r.json()["url"]
            content = requests.get(link).content
            return content

    def cuddle(link:bool):
        r = requests.get(base_url+"/cuddle")

        if link == True:
            link = r.json()["url"]
            return link
        if link == False:
            link = r.json()["url"]
            content = requests.get(link).content
            return content

class nsfw():
    def __init__(self):
        super().__init__()
    

    def hentai(link:bool):
        r = requests.get(base_url+"/nsfw/hentai")

        if link == True:
            link = r.json()["url"]
            return link
        if link == False:
            link = r.json()["url"]
            content = requests.get(link).content
            return content

    def boobs(link:bool):
        r = requests.get(base_url+"/nsfw/boobs")

        if link == True:
            link = r.json()["url"]
            return link
        if link == False:
            link = r.json()["url"]
            content = requests.get(link).content
            return content
            
def help():
    print(endpoints)
