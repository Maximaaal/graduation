import time
import os
import re
import json
import socket
from geolite2 import geolite2

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

if __name__ == '__main__':
    
    logfile = open("/var/log/pihole.log","r")
    loglines = follow(logfile)
    
    q = 0
    
    for line in loglines:
        pattern = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        pattern.remove('192.168.1.221')
        pattern = re.split(' ', line)
        print(pattern[7])
        
        try:
            ip = socket.gethostbyname(pattern[7])
            reader = geolite2.reader()
            respone = reader.get(ip)
            print(json.dumps(response['location']['latitude'], indent =4))
            print(json.dumps(response['location']['longitude'], indent =4))
        except socket.error:
            pass
        
        
               

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        