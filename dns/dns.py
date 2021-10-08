import time
import os
import re


def follow(thefile):
    '''generator function that yields new lines in a file
    '''
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)
    
    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line:
            time.sleep(0.1)
            continue

        yield line

if __name__ == '__main__':
    
    logfile = open("/var/log/pihole.log","r")
    loglines = follow(logfile)
    # iterate over the generator
    
    # for line in loglines:
    #     line = line.split(":",1)
    #     print(line, end='')

    
     
    # initializing the list object
    lst=[]
    
    #lst.append(pattern.search(line)[0])
    #print(lst, end='')
    
    for line in loglines:
        pattern = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        del pattern[0]
        print(pattern)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        