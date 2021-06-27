import hashlib
import time
from merkle import merkle_tree

class Blockchain:
    difficulty = 20
    maxNonce = 2**32
    target = 2**(256-difficulty) #If you are implementing a non 16 bit hashing algorithm please adjust 256 to whatever base you are using squared

    def __init__(self):
        """Initializes a BlockChain object with a set proof of work."""
        self.chain = [] #Change to doubly linked list later
        self.current_transactions = []
        self.new_block(previous_hash="Genesis", proof="sha_256")

    def add(self, block):
        """Adds a block to the BlockChain object."""
        block.previous_hash = self.block.hash(self.pow)
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next
        self.tail = self.block

    def new_block(self, proof, previous_hash=None):
        """Generates a new block for use in the blockchain"""
        merkle_tree = merkle_tree(self.current_transactions)
        merkle_tree.verify(merkle_tree.root, self.current_transactions)
        block = {
            'index': len(self.chain) + 1,
            'timestamp' : time.time(),
            'transactions': merkle_tree.root_hash(), 
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions=[] #Sets the current transaction list to empty.
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Creates a new transaction for use in the current block."""
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

    def hash(self, block, nonce=0):
        """Creates a hashcode for the a block using its parts and a nonce."""
        h = hashlib.sha256()
        h.update(
            str(nonce).encode('utf-8') +
            str(block['index']).encode('utf-8') +
            str(block['transactions']).encode('utf-8') + 
            str(block['timestamp']).encode('utf-8') +
            str(block['previous_hash']).encode('utf-8') 
        )

        return h.hexdigest()

    def proof_of_work(self, block):
        """Mines by checking if the hashed block is smaller than or equal to the target size after adjusting the hash to the correct base. 
        If not it rehashes the current block."""
        nonce = 0
        while int(self.hash(block, nonce), 16) <= self.target > self.target:
            nonce += 1
        
    def history(self):
        """Prints all blocks within the generated BlockChain, 
        The Genesis block does not need to be mined as its hash is 0 and thus is not listed during the mining process."""
        for i in self.chain:
            print(i)

    def update(self, blockchain_obj):
        """Updates BlockChain based on which BlockChain is longer."""
        if len(self.chain) > len(blockchain_obj.chain):
            blockchain_obj.chain = self.chain
        elif len(blockchain_obj.chain) > len(self.chain):
            self.chain = blockchain_obj.chain

