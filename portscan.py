import socket

host = "www.google.com"
ports = [80,443,21,22]


for port in ports:
    #creating tcp client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connecting
    response = client.connect_ex((host, port))

    if response == 0:
        print(f"[+]{port} is open")
    
