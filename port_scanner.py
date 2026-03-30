import socket
from datetime import datetime, timezone
import random
from uuid import uuid4
import concurrent.futures




def scanning(ip, ports, timeout=2, sid=None, timestamp=None):
    
    if sid is None:
        sid = str(uuid4())

    if timestamp is None:
        timestamp = datetime.now(timezone.utc).isoformat()    

    try:

        client = None
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        response = client.connect_ex((ip, ports))
        if response == 0:
            print(f"'[+]Port {ports} is open from {target} ")
        else:
            print(f'[+]Port {ports} is closed/filtered from {target} ')
    except KeyboardInterrupt:
        print(f'[+]Scanner interrupted.')
    except Exception as e:
        print(f'[+]Error: {e} is occurred')
    finally:
        if client:
            client.close()




#Set the target
target = "google.com"
ports = list((range(1,1025)))
random.shuffle(ports)

#Getting IPV4 and DNS treatment.
ip = None
try:
    ip = socket.gethostbyname(target)

except socket.gaierror:
    print(f'[+]Hostname {target} does not exists, fix it or check your DNS server')
    exit()
        
#Setting workers to assync scanning
with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
   f = {executor.submit(scanning,ip,port): port for port in ports}
   for future in concurrent.futures.as_completed(f):
       port = f[future]
       try:
           data = future.result()
       except Exception as exc:
           print(f'{port} generated an exception: {exc}')
       except KeyboardInterrupt:
           executor.shutdown(wait=False, cancel_futures=True)
           print(f'[+]Scanner interrupted.')
