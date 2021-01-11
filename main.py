from block import block
from blockchain import blockchain

pow = "keccak_256" #This is the proof of work being utilized in the BlockChain
blockchain = blockchain(pow)
#Mines blocks within the BlockChain using "Block " + str(n+1) as the data to be hashed
for n in range(10):
    print("Mining Block " + str(n+1) + "\n")
    blockchain.mine(block("Block " + str(n+1)))

#Prints all blocks within the generated BlockChain, The Genesis block does not need to be mined as its hash is 0 and thus is not listed during the mining process
print("All blocks in the BlockChain:\n")
blockchain.history()