import socket
import time
import random
import concurrent.futures



def scanning(ip, port, timeout=2):
    

    try:

        client = None
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        response = client.connect_ex((ip, port))
        if response == 0:
            print(f"[+]Port {port} is open from {host}")
        else:
            print(f'[+]Port {port} is closed/filtered from {host} ')
    except KeyboardInterrupt:
        print(f'[+]Scanner interrupted.')
    except Exception as e:
        print(f'[+]Error: {e} is occurred')
    finally:
        if client:
            client.close()

host = "www.google.com"

#Get IPV4 and DNS treatment.
ip = None
try:
    ip = socket.gethostbyname(host)

except socket.gaierror:
    print(f'[+]Hostname {host} does not exists, fix it or check your DNS server')
    exit()
    

port = 443

#Setting workers to assync scanning
with ThreadPoolExecutor(max-workers=100) as executor:
    future = executor.submit

scanning(ip,port)
ports = list((range(1,1025)))
random.shuffle(ports)
    
    
    
    











#time = time.end()