from datasructures.linkedList import LinkedList


def merge_sort(linked_list: LinkedList):
    """
      sorts a linked list in ascending order
      - Recursively divide the linked list int sublists containing a single node
      - Repeatedly merge the sublists to produce sorted sublists until one remains
      
      Returns a sorted linked list 
      
      Runs in O(kn log n)
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)
    
def split(linked_list: LinkedList):
    """
     Devide the unsorted list at midpoint into sublists
     Takes O(k log n)
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        
        return left_half, right_half
    
    size = linked_list.size()
    mid = size // 2
    
    mid_node = linked_list.node_at_index(mid-1)
    
    left_half = linked_list
    right_half = LinkedList()
    right_half.head = mid_node.next_node
    mid_node.next_node = None
    
    return left_half,  right_half
    
def merge(left, right):
    """
     Merges two linked lists, sorting by data in nodes
     Returns a new merged list
    """
    # Create a new linked list that contains nodes from mergin left and right
    
    merged = LinkedList()
    
    #Add a fake head that is discarded later
    
    merged.add(0)
    
    #set current to the head of the linked list 
    
    current = merged.head
    
    left_head = left.head
    right_head = right.head
    
    # Iterate over left and right until we reach the tail node
    # of either 
    while left_head or right_head:
        # If the head node of the left is None, we're past the tail
        # Add the node from right to merged linked list
        
        if left_head is None:
            current.next_node = right_head
            
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
            
        # If the head node of the right is None, we're past the tail
        # Add the tail node from left to merged linked list
        
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            #Not at either tail node
            # Obtain node data to perfom comparison operations
            left_data = left_head.data
            right_data = right_head.data

            #If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                #move left head to next node
                left_head = left_head.next_node
                
            else:
                current.next_node = right_head
                # move right head to next node
                
                right_head = right_head.next_node
                
        # Move current to next node
        current = current.next_node
        
    # discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    
    return merged
    
lk = LinkedList()

import random

x = 0
while x != 1000:
    x = random.randint(1, 10001)
    lk.add(x)

print(merge_sort(lk))