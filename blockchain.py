from block import block
import datetime

class blockchain:
    difficulty = 20
    maxNonce = 2**32
    target = 2**(256-difficulty) #If you are using a non 16 bit hashing algorithm please adjust 256 to whatever base you are using squared

    block = block("Genesis")
    temp = head = block

    def __init__(self, pow="sha_256"):
        """Initializes a BlockChain object with a set proof of work."""
        self.pow = pow

    def add(self, block):
        """Adds a block to the BlockChain object."""
        block.previous_hash = self.block.hash(self.pow)
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        """Mines by checking if the hashed block is smaller than or equal to the target size after adjusting the hash to the correct base. 
        If not it rehashes the current block."""
        for n in range(self.maxNonce):
            if int(block.hash(self.pow), 16) <= self.target: #If you are using a non 16 bit hashing algorithm please adjust 16 to whatever base you are using
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

    def history(self):
        """Prints all blocks within the generated BlockChain, 
        The Genesis block does not need to be mined as its hash is 0 and thus is not listed during the mining process."""
        current = self.head
        while current is not None:
            print(current)
            current = current.next

    def traverse(self):
        """Traverses the BlockChain and returns the number of blocks in the BlockChain."""
        n = 0
        current = self.head
        while current is not None:
            n += 1
            current = current.next
        return n

    def update(self, blockchain_obj)
        """Updates BlockChain based on which BlockChain is longer (starting at block 0)."""
        if(self.traverse() < blockchain_obj.traverse()):
            current = self.head
            current_other = blockchain_obj.head
            while current_other is not None:
                temp = current = current_other
                current_other = current_other.next
                current = current.next
        elif (self.traverse() > blockchain_obj.traverse()):
            current = self.head
            current_other = blockchain_obj.head
            while current is not None:
                temp = current_other = current
                current_other = current_other.next
                current = current.next

