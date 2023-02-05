from client import Client

if __name__ == "__main__":
    print("Use the bitcoin-protocol client here...")
    client = Client("137.226.34.46", 8333)
    version = client.connect()
    print("Version :", version, end="\n\n")

    pong = client.ping()
    print("Pong :", pong)