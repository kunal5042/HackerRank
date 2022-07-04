# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(head, data, position):
    node = head
    
    while position > 1:
        node = node.next
        position -= 1
        
    next = node.next
    node.next = SinglyLinkedListNode(data)
    node.next.next = next
    
    return head

# Kunal Wadhwa
