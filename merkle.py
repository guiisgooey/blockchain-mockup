from node import node
import hashlib

class merkle_tree():
    def __init__(self):
        self.root = None

    def hash(self, item):
        return hashlib.sha256(item.encode('utf-8')).hexdigest()

    def construct(self, transactions):
        current_level = []
        previous_level = [node(hash(i)) for i in transactions] #leaves
        while len(previous_level) > 1:
            for i in range (0,len(previous_level), 2):
                current_node = node()
                current_node.left = previous_level[i]
                if i+1 < len(previous_level):
                    current_node.right = previous_level[i+1]
                    current_node.data = hash(previous_level[i].data + previous_level[i+1].data)
                else:
                    current_node.data = hash(previous_level[i].data)
                current_level.append(current_node)
            previous_level = current_level
            current_level = []
        self.root = current_level[0] #will only have len of 1 anyways

    def verify(self):
        current = [self.root] #basically used as a queue for bfs of the nodes
        for i in current:
            while hasattr(current, 'left'):
                if current.right:
                    assert current.data == hash(current.left.data + current.right.data)
                    current.pop()
                    current.append(current.left, current.right)
                else:
                    assert current.data == hash(current.left.data)
                    current.pop()
                    current.append(current.left)
