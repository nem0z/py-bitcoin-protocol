import random
from message import Message

def message(nonce=0):
    payload = (nonce if nonce else random.getrandbits(64))
    payload = payload.to_bytes(8, byteorder="little", signed=False)
    return Message("ping", payload)