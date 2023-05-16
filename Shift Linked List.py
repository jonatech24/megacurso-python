#WWrite a function that takes in the head of a single linked list and an integer k, 
#shifts the list in place (i.e., doesn't create a brand-new list) by k position, and returns its new head.
#Shifting a Linked List means moving its nodes forward or backward and wrapping them around the list where appropriate. 
#For example, shifting a linked list forward by one position would make its tails become the new head of the linked list.
#Whether nodes are moved forward or backward is determined by whether k is positive or negative.
#Each linked list node has an integer value as well as a next node pointing to the next node in the list
# or to None / null if it's the tail of the list.
#You can assume that the input List will always have at least one node; in other words, the head will 
#never be None / null.

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Write your code here.
    # Get the length of the linked list
    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1
    
    # Handle the case where k is greater than the length of the linked list
    k = k % length
    
    # Handle the case where k is negative
    if k < 0:
        k = length + k
    
    # Handle the case where k is zero
    if k == 0:
        return head
    
    # Find the new tail and the new head
    new_tail = head
    for i in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    
    # Set the new tail to None
    new_tail.next = None
    
    # Set the old tail to point to the old head
    tail.next = head
  
    # Return the new head
    return new_head

    pass