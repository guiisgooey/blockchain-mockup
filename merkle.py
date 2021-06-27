import hashlib

class merkle_tree():
    def __init__(self, transactions):
        """Initializes a new Merkle tree"""
        self.root = None
        self._transactions = transactions
        self._construct() #automatically constructs tree using provided transactions

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
        self.root = current_level[0] #will only have len of 1 anyways
    
    def consistency_proof(self, head):
        """Verifies the previous records are untampered with when new records are added.
        A copy of the head of the tree must be saved by the client to utilize this."""
        current = [head] #basically used as a queue for bfs of the nodes
        for i in current:
            while current['left']: #leaves left value equals None which will read as False
                if current['right']:
                    assert current.data == hash(current['left']['data'] + current['right']['data'])
                    current.pop()
                    current.append(current['left']) #appends left and right children to the queue
                    current.append(current['right'])
                else:
                    assert current.data == hash(current['left']['data'])
                    current.pop()
                    current.append(current['left']) #appends left child to the queue
        transactions = [self.node(i) for i in self.transactions] #creates a list of nodes that contain transactions as data to compare with the leaves of the tree
        transactions = transactions[:len(current)] #we only want to check the common leaves the two trees share
        assert current == transactions
    
    def root_hash(self):
        """Returns the hash value of the mother node / root of the Merkle tree."""
        return self.root.data
