import os

def rootkit():
 try:
  print'rootkit scanner(scanning for rootkits,trojans,malicious files)'
  print'downloading required rootkit (clamav)'
  os.system('apt-get install rkhunter')
  os.system('rkhunter -c')
  print'DONE!!!!!!'
 except:
  print"rootkithunter couldn't be initiated due to an error ,\n.skiiping it!!"
