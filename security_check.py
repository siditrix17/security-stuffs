#import subprocess
import os
def lyni():
 try:
  os.system("apt-get install lynis") #those who don't have lynis
  os.system("lynis -c -Q")
  #subprocess.call("lynis -c -Q")
 except:
  print"security_check couldn't be performed!!"
