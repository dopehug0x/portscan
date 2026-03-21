import socket
import time



def scanning(link, port, time=2):

    try:

        client = None
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response = client.connect_ex((link, port))
        if response == 0:
            print(f"[+]Port {port} is open from {link}")
            return None
        else:
            print(f'[+]Port {port} is closed/filtered from {link} ')
            return None
    except Exception as e:
        print(f'Error: {e} is occurred')
        return None
    finally:
        client.close()

link = "www.google.com"
port = 22

scanning(link,port)
#ports = list(range(1,1025))

    
    
    
    











#time = time.end()