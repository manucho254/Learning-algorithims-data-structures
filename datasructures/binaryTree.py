
class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
    def add(self, value):
        node = BinaryTree(value)
            
        if value > self.value:
            if self.left is None:
                self.left =  node
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right =  node
            else:
                self.right.add(value)
    
    def __repr__(self) -> str:
        nodes = []
        current = self.value
        right = self.right
        left = self.left
        
        while left:
            nodes.append("%s" % left.value)
            left = left.left
        
        nodes.append("%s" % current)
        
        while right:
            nodes.append("%s" % right.value)
            right = right.right
            
        return "-> ".join(nodes)
    
        
tree = BinaryTree(2)
tree.add(1)
tree.add(3)
tree.add(4)
tree.add(9)

print(tree)