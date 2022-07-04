#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    stack = []
    # put all the nodes in a stack
    while llist is not None:
        stack.append(llist)
        llist = llist.next
        
    # pop the last node from the stack
    head = stack.pop()
    head_reference = head
    
    # pop all the nodes and connect them with the reversed linked list
    while len(stack) != 0:
        head.next = stack.pop()
        head = head.next
        
    # point the last node to NULL
    head.next = None
    
    # return head
    return head_reference

# Kunal Wadhwa
