#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):

    while llist is not None:
        # this is current's next
        next = llist.next
        
        # before moving to the next node, swap current's left with previous
        llist.prev, llist.next = llist.next, llist.prev
        
        # if it's the last node, current's next will be NULL
        if next is None:
            break
        
        # move to the next node
        llist = next
        
    return llist


# Kunal Wadhwa
