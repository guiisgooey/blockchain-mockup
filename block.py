import datetime
import hashlib
import sha3

class block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = hex(0)
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now()

    def hash(self):
        h = sha3.keccak_256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8') 
        )
        return h.hexdigest()
    
    def __str__(self):
        return "[" + str(self.timestamp) + "]\nBlock Hash: " + str(self.hash()) + "\nBlock #: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\n# Hashes: " + str(self.nonce) + "\n"