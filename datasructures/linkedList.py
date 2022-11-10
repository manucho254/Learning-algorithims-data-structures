class Node:
    """
      An object for storing a single node of a linked list
      models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None
    
    def __init__(self, data) -> None:
        self.data = data
        
    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data
    
    
class LinkedList:
    """ Singly linked list """
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """ 
        Returns the number of nodes in the list
        Takes O(n) time linear time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data: int):
        """ Adds new Node containing data at the head of the list 
        Takes O(1) constant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self, key):
        """ 
        Search for the first node containing data that matches the key
        Returns the node or `None` if key not found 
        Takes O(n) linear time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next_node
            
    def insert(self, data: int, index: int):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) constant time but finding the node at the insertion
        point takes O(n) linear time
        
        Takes Overall O(n) linear time for insertion
        """
        if index == 0:
            self.add(data)
            
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = current.next_node
                position -= 1
                
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new
            new.next_node = next_node
            
    
    def remove(self, key: int):
        """
          Removes Node containing data that matches the key
          Returns the mode or None if key doesn't exists
          Takes O(n) linear time
        """
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found =True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
                
        return current
                
    def node_at_index(self, index):
        if index == 0:
            return self.head
        current = self.head
        position = 0
        
        while position < index:
            current = current.next_node
            position += 1
        return current
        
    def __repr__(self) -> str:
        """
        Return a string representation of the list 
        Takes O(n) time
        """
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("%s" % current.data)
            current = current.next_node
            
        return "-> ".join(nodes)
        
  
l = LinkedList()  

#naive way of adding to a linked list    
n1 = Node(10)
l.head = n1
n2 = Node(20)
l.head.next_node = n2
n3 = Node(30)
l.head.next_node.next_node = n3
n4 = Node(40)
l.head.next_node.next_node.next_node = n4

#better way to adding to a linked list

l.add(100)
l.insert(200, 3)
print(l)
print(l.search(10))
print(l.size())


