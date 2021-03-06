#!/usr/bin/env python
import os
import socket
import subprocess
import commands
import sys
from datetime import datetime

def portsca():

 # Clear the screen
 subprocess.call('clear', shell=True)

 # Ask for input
 print"-- Port scanner --"
 os.system('netstat -tulpn')
 r=raw_input('wanna scan remote host y/n :')
 if r=='y':
  print'**info--(enter remote host if you wanna scan : \n)'
  u=raw_input('ip :')
  remoteServerIP  = socket.gethostbyname(u)
  # Print a nice banner with information on which host we are about to scan
  print "-" * 80
  print "Please wait, scanning remote host", remoteServerIP
  print "-" * 80

  # Check what time the scan started
  t1 = datetime.now()


  # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

  # We also put in some error handling for catching errors

  try:
     for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)       
        sock.close()
     print'No ports opened'
  except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    

  except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
  
  except socket.error:
    print "Couldn't connect to server"
 else:
   print'aborting remote host scan!'  
