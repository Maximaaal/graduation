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
import ipinfo

pygame.init()
pygame.font.init()

X = 1920
Y = 1080

with open('apikey.txt', 'r') as file:
    api_key = file.read().replace('\n', '')
print(api_key)

url = "https://maps.googleapis.com/maps/api/staticmap?"
center = "New York"

acces_token = '113cd6b84c34a4'
handler = ipinfo.getHandler(acces_token)

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
        #pattern.remove('192.168.1.184')
        pattern = re.split(' ', line)
        print(Fore.WHITE + pattern[7])
        #print(Style.RESET_ALL)
        
        try: 
            hostname = pattern[7]
            ip_address = socket.gethostbyname(hostname)
            print(ip_address)
            details = handler.getDetails(ip_address)
            print(details.loc)
            center = details.loc
            city = details.city
            #r = request.get(url + "center =" + center + "&zoom =" + str(zoom) + api_key + "sensor = false")
            r = requests.get(url + "center=" + center + "&zoom=" +
                 str(zoom) + "&maptype=satellite" + "&scale=2" + "&size=400x400&key=" +
                 api_key)
            f = open('sat', 'wb')
            f.write(r.content)
            f.close()
            myfont = pygame.font.SysFont(None, 70)
            display_surface = pygame.display.set_mode((X, Y))
            #display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-2, -30)
            image = pygame.image.load('sat')
            textsurface = myfont.render(city, True, (255, 255, 255))
            locText =  myfont.render(center, True, (255, 255, 255))
            text_rect = textsurface.get_rect(center=(X/2, 60))
            display_surface.blit(image, (((X / 2) - 400), ((Y / 2) - 400)))
            #display_surface.blit(textsurface, (0, 0))
            display_surface.blit(textsurface, (10, 0))
            display_surface.blit(locText, (10, 50))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            pygame.display.update()
        except Exception:
            pass
    













