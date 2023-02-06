import hashlib

def checksum(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]

def to_bytes_fixed_size(data, size):
    return bytes.fromhex(data.hex() + "00"*(size-len(data)))