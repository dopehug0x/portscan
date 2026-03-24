import socket
import datetime
import random
from uuid import uuid4
import concurrent.futures




def scanning(ip, port, timeout=2, sid=None, timestamp=None):
    

    try:

        client = None
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sid = uuid4()
        client.settimeout(timeout)
        response = client.connect_ex((ip, port))
        if response == 0:
            print(f"[+]Port {port} is open from {host} | {sid} session.")
        else:
            print(f'[+]Port {port} is closed/filtered from {host} ')
    except KeyboardInterrupt:
        print(f'[+]Scanner interrupted.')
    except Exception as e:
        print(f'[+]Error: {e} is occurred')
    finally:
        if client:
            client.close()




#Set the target
host = "186.192.83.5"
port = 80

#Getting IPV4 and DNS treatment.
ip = None
try:
    ip = socket.gethostbyname(host)

except socket.gaierror:
    print(f'[+]Hostname {host} does not exists, fix it or check your DNS server')
    exit()
    



#Socket id
sid = None
if sid is None:
    str(uuid4())

#timestamp
timestamp = None
if timestamp is None:
    str(datetime.isoformat())

#Setting workers to assync scanning
#with ThreadPoolExecutor(max-workers=100) as executor:
 #   future = executor.submit

scanning(ip,port)
ports = list((range(1,1025)))
random.shuffle(ports)
    
    
    
    











#time = time.end()