from block import block
from blockchain import blockchain
import datetime

blockchain = blockchain()

for n in range(10):
    blockchain.mine(block("Block " + str(n+1)))

while blockchain.head is not None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next 
