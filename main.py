import time 

from client import Client

if __name__ == "__main__":
    ipv4 = "23.88.68.160"
    ipv6 = "2a01:04f8:0201:2383:0000:0000:0000:0002"
    client = Client(ipv6, 8333)
    version = client.connect()

    pong = client.ping()
    print("Pong :", pong)
    
    list_addr = client.getaddr()
    print(list_addr[0] if len(list_addr) > 0 else None)