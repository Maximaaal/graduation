import time
import os
import re
import json
import socket


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
    
    for line in loglines:
        pattern = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        pattern.remove('192.168.0.176')
        string = "reply"
        pattern = re.split(' ', line)
        print(pattern[7])
        
        try:
            print(colors.YELLOW + socket.gethostbyname(pattern[7]) + colors.ENDC)
        except socket.error:
            pass
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        