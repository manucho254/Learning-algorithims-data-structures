class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self):
        self.head = None
        
    def add(self, val):
        node = TreeNode(val)
            
        if self.head == None:
            self.head = node
        else:
            if val > self.head.val:
                self.head.right = node
            else:
                self.head.left = node
                
        return self.head
    
    def __repr__(self) -> str:
        nodes = []
        current = self.head
        right = self.head.right
        left = self.head.left
        
        while left:
            nodes.append("%s" % left.val)
            left = left.left
            
        nodes.append("%s" % current.val)
        
        while right:
            nodes.append("%s" % right.val)
            right = right.right
            
        return "-> ".join(nodes)
    
        
tree = BinaryTree()
tree.add(2)
tree.add(1)
tree.add(3)
tree.add(3)
tree.add(4)

print(tree)