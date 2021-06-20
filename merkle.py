from node import node
import hashlib
class merkle_tree():
    def __init__(self):
        self.left = None
        self.right = None
        self.root = None

    def hash(self, item):
        return hashlib.sha256(item.encode('utf-8')).hexdigest()

    def build_tree(self, transactions):
        current_level = []
        previous_level = [hash(i) for i in transactions]
        while len(previous_level) > 1:
            for i in range (0,len(previous_level), 2):
                current_node = node()
                current_node.left = previous_level[i]
                if i+1 <= len(previous_level)-1:
                    current_node.right = previous_level[i+1]
                    current_node.data = hash(previous_level[i] + previous_level[i+1])
                else:
                    current_node.data = hash(previous_level[i])
                current_level.append(current_node)
            previous_level = current_level

            current_level = []
        self.root = current_level[0]

    def verify(self):
        pass