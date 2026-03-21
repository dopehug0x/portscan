import socket
import time




def scanning(host, port, timeout=2):
    
    try:

        client = None
        ip = socket.gethostbyname(host)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        response = client.connect_ex((ip, port))
        if response == 0:
            print(f"[+]Port {port} is open from {host}")
        else:
            print(f'[+]Port {port} is closed/filtered from {host} ')
    except KeyboardInterrupt:
        print(f'[+]Scanner interrupted.')
    except socket.gaierror: #DNS error
        print(f'[+]Hostname {host} doesnt exists.')
    except Exception as e:
        print(f'[+]Error: {e} is occurred')
    finally:
        if client:
            client.close()

host = "www.googliurieiiaiaii.com"
port = 22

scanning(host,port)
#ports = list(range(1,1025))

    
    
    
    











#time = time.end()