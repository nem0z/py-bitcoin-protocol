import socket
import time

import utils
from message import Message


def message(peer_ip_str, peer_port=8333):
    # Version number (PROTOCOL_VERSION in core)
    version = int(70015).to_bytes(4, 'little')

    # Random services, we don't care
    services = int(1).to_bytes(8, 'little')

    timestamp = int(time.time()).to_bytes(8, 'little')
    client_ip_str = "127.0.0.1"
    client_ip = socket.inet_aton(client_ip_str)
    peer_ip = socket.inet_aton(peer_ip_str)

    addr_recv = utils.to_bytes_fixed_size(services, 19) + b'\xff\xff'
    addr_recv += peer_ip + int(peer_port).to_bytes(2, 'big')
    addr_from = utils.to_bytes_fixed_size(services, 19) + b'\xff\xff'
    addr_from += client_ip + int(8333).to_bytes(2, 'big')
    nonce = 0x00.to_bytes(8, 'little')

    # You can replace this with something more fun
    user_agent = 0x00.to_bytes(1, 'big')
    # Let's say zero, once again we don't care for this example
    start_height = 0x00.to_bytes(4, 'little')

    payload = (
        version 
        + services
        + timestamp 
        + addr_recv 
        + addr_from 
        + nonce 
        + user_agent 
        + start_height
    )

    return Message("version", payload)