import os

def rootkit():
 print'rootkit scanner(scanning for rootkits,trojans,malicious files)'
 print'downloading required rootkit (clamav)'
 os.system('apt-get install rkhunter')
 os.system('rkhunter -c')
 print'DONE!!!!!!'
