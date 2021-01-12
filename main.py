from block import block
from blockchain import blockchain

pow = "keccak_256" #This is the proof of work being utilized in the BlockChain
blockchain1 = blockchain(pow)
blockchain2 = blockchain(pow)

#Mines blocks within the BlockChain using "Block " + str(n+1) as the data to be hashed
print("----MINING BLOCKCHAIN1----\n")
for n in range(4):
    print("Mining Block " + str(n+1) + "\n")
    blockchain1.mine(block("Block " + str(n+1)))

#Prints all blocks within the generated BlockChain, The Genesis block does not need to be mined as its hash is 0 and thus is not listed during the mining process
print("----PRINTING BLOCKCHAIN1----\n")
print("All blocks in the BlockChain:\n")
blockchain1.history()


#Mines blocks in blockchain2
print("----MINING BLOCKCHAIN2----\n")
for n in range(5):
    print("Mining Block " + str(n+1) + "\n")
    blockchain2.mine(block("Block " + str(n+1)))

#Updates blockchain to become blockchain2 as blockchain2 is larger
print("----UPDATING BLOCKCHAIN1----\n")
blockchain1.update(blockchain2)

print("----REPRINTING BLOCKCHAIN1----\n")
print("All blocks in the BlockChain:\n")
blockchain1.history()