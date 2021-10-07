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

    pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)
{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
 
# initializing the list objects
valid =[]
invalid=[]
 
# extracting the IP addresses
for line in loglines:
    line = line.rstrip()
    result = pattern.search(line)
 
    # valid IP addresses
    if result:
      valid.append(line)
 
    # invalid IP addresses 
    else:
      invalid.append(line)
 
# displaying the IP addresses
print("Valid IPs")
print(valid)
print("Invalid IPs")
print(invalid)

        