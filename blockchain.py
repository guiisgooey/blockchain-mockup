from block import block

class blockchain:
    difficulty = 20
    maxNonce = 2**32
    target = 2**(256-difficulty)

    block = block("Genesis")
    dummy = head = block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

