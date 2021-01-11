import datetime
from hashlib import sha256, scrypt
from sha3 import keccak_256

class block:
    blockNo = 0
    data = None
    next = None
    hash = None
    pow = None
    nonce = 0
    previous_hash = hex(0)
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        """Initializes a new block object with set data."""
        self.data = data

    def hash(self, pow):
        """creates a hash object and updates the object with information from the block."""
        if self.nonce == 0:
            self.pow = pow

        h = sha256()
        if (pow.lower() == "keccak_256" or pow.lower() == "keccak256" or pow.lower() == "keccak-256"):
            h = keccak_256()
        elif (pow.lower() == "scrypt"):
            pass

        self.timestamp = datetime.datetime.now()

        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8') 
        )

        return h.hexdigest()
    
    def __str__(self):
        """Returns a string representation of the block object with the timestamp of acception, the accepted hash, 
        the block number, the block's data, and the number of hashes it took to find an acceptable hash."""
        return "Timestamp: [" + str(self.timestamp) + "]\nAccepted Hash: " + str(self.hash(self.pow)) + "\nBlock Num: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nNum Hashes: " + str(self.nonce) + "\n"