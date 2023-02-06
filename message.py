import hashlib

import utils

class Message:
    def __init__(self, command_name, payload):
        self.magic_number = bytes.fromhex("f9beb4d9")
        self.command_name = utils.to_bytes_fixed_size(command_name.encode("ascii"), 12)
        self.payload = payload
        self.length = (int(len(payload))).to_bytes(4, byteorder="little", signed=False)
        self.checksum = utils.checksum(payload)

    def get(self):
        return (
            self.magic_number
            + self.command_name
            + self.length
            + self.checksum
            + self.payload
        )
