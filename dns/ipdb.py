import traceback
import sys
import time
import os
import re
import socket
from geolite2 import geolite2
import json
import colorama
from colorama import Fore, Style
import requests
import pygame

pygame.init()
X = 800
Y = 700

with open('apikey.txt', 'r') as file:
    api_key = file.read().replace('\n', '')
print(api_key)

url = "https://maps.googleapis.com/maps/api/staticmap?"
center = "New York"

zoom = 13

def follow(thefile):

    thefile.seek(0, os.SEEK_END)

    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue

        yield line

class colors:
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    GREEN = '\033[92m'
    
amount = 0

if __name__ == '__main__':
    
    logfile = open("/var/log/pihole.log","r")
    loglines = follow(logfile)
    
    for line in loglines:
        pattern = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        pattern.remove('192.168.1.221')
        pattern = re.split(' ', line)
        print(Fore.WHITE + pattern[7])
        amount = amount + 0.0002833333
        print(Fore.GREEN + "$",amount)
        #print(Style.RESET_ALL)
        
        
        
        try: 
            hostname = pattern[8]
            ip_address = socket.gethostbyname(hostname)
            print(Fore.WHITE + ip_address)
            reader = geolite2.reader()
            response = reader.get(ip_address)
            #print(json.dumps(response['continent']['names']['en'],indent =4))
            cityName = json.dumps(response['city']['names']['en'],indent =4)
            print(Fore.YELLOW + cityName)
            print(" ")
            #print(json.dumps(response['location']['time_zone'],indent =4))
            newLat = json.dumps(response['location']['latitude'],indent =4)
            newLon = json.dumps(response['location']['longitude'],indent =4)
            print(newLat, newLon)
            #r = request.get(url + "center =" + center + "&zoom =" + str(zoom) + api_key + "sensor = false")
            center = cityName
            r = requests.get(url + "center=" + center + "&zoom=" +
                 str(zoom) + "&maptype=satellite" + "&scale=2" + "&size=400x400&key=" +
                 api_key)
            f = open('yee', 'wb')
            f.write(r.content)
            f.close()
            
            display_surface = pygame.display.set_mode((X, Y))
            image = pygame.image.load('yee')
            display_surface.blit(image, (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            pygame.display.update()
        except Exception:
            pass
    














