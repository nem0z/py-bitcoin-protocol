import time 

from client import Client

if __name__ == "__main__":
    client = Client("178.83.160.129", 8333)
    version = client.connect()

    pong = client.ping()
    print("Pong :", pong)
    
    list_addr = client.getaddr()
    print(list_addr[0] if len(list_addr) > 0 else None)