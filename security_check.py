#import subprocess
import os
def lyni():
 os.system("apt-get install lynis") #those who don't have lynis
 os.system("lynis -c -Q")
#subprocess.call("lynis -c -Q")

