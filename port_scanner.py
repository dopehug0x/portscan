import socket
import time



def scanning(link, port, time=2):
    client = None
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response = client.connect_ex((link, port))
    if response == 0:
        print(f"[+]Port {port} is open from {link}")
        client.close()
        return None
    else:
        print(f'[+]Port {port} is closed/filtered from {link} ')
        client.close()
        return None

link = "www.google.com"
port = 22

scanning(link,port)
#ports = list(range(1,1025))

    
    
    
    











#time = time.end()