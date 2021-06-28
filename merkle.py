import hashlib

class merkle_tree():
    def __init__(self, transactions):
        """Initializes a new Merkle tree"""
        self.root = self._construct(transactions) #automatically constructs tree using provided transactions

    @staticmethod
    def hash(item):
        """Hashes the specified item using SHA-256."""
        return hashlib.sha256(item.encode('utf-8')).hexdigest()

    @staticmethod
    def node(data=None, left=None, right=None):
        """Creates a new node for use in the Merkle tree using a dictionary."""
        node = {
            'data': data,
            'left': left,
            'right': right,
        }
        return node

    def _construct(self):
        """Constructs a Merkle tree given the list of transactions."""
        current_level = []
        previous_level = [self.node(hash(i), self.node(i)) for i in self._transactions] #leaves
        while len(previous_level) > 1:
            for i in range (0,len(previous_level), 2):
                current_node = self.node(hash(previous_level[i].data), previous_level[i]) #preset data to using the hash of previous data
                if i+1 < len(previous_level): #if i+1 exceeds the length of the previous level, we cannot combine two previous datas to hash
                    current_node['right'] = previous_level[i+1]
                    current_node['data'] = hash(previous_level[i].data + previous_level[i+1].data) #if there is an available right node, data must be combination hash
                current_level.append(current_node)
            previous_level = current_level
            current_level = [] 
        return current_level[0] #will only have len of 1 anyways
    
    def inclusion_proof(self):
        pass
    
    def consistency_proof(self, head):
        """Verifies the previous records are untampered with when new records are added.
        A copy of the head of the tree must be saved by the client to utilize this."""
        t2 = self.get_transactions(self.root) #gets transactions from current, updated tree
        t1 = self.get_transactions(head) #gets transactions from original tree
        for i in range(t1):
            assert t2[i] == t1[i] #checks that all items before new additions in tree 2 are identical to those in tree 1
        t3 = t1.extend(t2[:len(t1)])
        assert self._construct(t3) == self.root #checks that if all new items in tree 2 were added to tree 1, the root would be identical
    
    @staticmethod
    def get_transactions(head):
        current = [head] #used as a queue for bfs of the nodes
        for i in current:
            while i['left']: #if nodes left value equals None which will read as False, and is guaranteed to be a leaf
                current.append(i['left']) #appends left child to the queue
                if i['right']:
                    current.append(i['right']) #appends right child to the queue
                current.pop()
        return current

    def root_hash(self):
        """Returns the hash value of the mother node / root of the Merkle tree."""
        return self.root.data
