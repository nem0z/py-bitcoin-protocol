import hashlib

def checksum(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]

def to_bytes_fixed_size(data, size):
    return bytes.fromhex(data.hex() + "00"*(size-len(data)))

def parse_var_int(first_9_bytes):
    first_byte = first_9_bytes[0]
    if first_byte < 0xFD:
        return 1, int.from_bytes(first_byte, 'little')
    elif first_byte == 0xFD:
        return 3, int.from_bytes(first_9_bytes[1:3], 'little')
    elif first_byte == 0xFE:
        return 5, int.from_bytes(first_9_bytes[1:5], 'little')
    elif first_byte == 0xFF:
        return 9, int.from_bytes(first_9_bytes[1:9], 'little')
    else:
        raise ValueError("Invalid first byte for var_int")
    
def chunk_to_list(data, chunk_size=30):
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def ip_to_string(bytes_ip):
    return '.'.join(str(b) for b in bytes_ip)

def parse_ip(data):
    ipv4 = data[-4:]
    ipv6 = data[:12] + bytes(16) + bytes(16) + data[-4:]
    return ip_to_string(ipv4), ip_to_string(ipv6)

def parse_addr(addr):
    return (
        int.from_bytes(addr[:4], "little"),     # timestamp
        int.from_bytes(addr[4:12], "little"),   # version (features enable)
        parse_ip(addr[12:28]),                  # ip_adress
        int.from_bytes(addr[28:30], "big"),     # port
    )