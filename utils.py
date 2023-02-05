def to_bytes_fixed_size(data, size):
    return bytes.fromhex(data.hex() + "00"*(size-len(data)))