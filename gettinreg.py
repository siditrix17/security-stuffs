import requests
req=requests.get("http://172.16.0.1:8090")
print'req code = \n' +str(req.status_code)
print'-----------------------------------'
print 'banner : \n'
e=req.text
file=open("c:/python27/new.txt",'w')
file.write(e)
file.close()
