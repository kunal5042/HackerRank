#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
def sortedInsert(llist, data):
    # Write your code here
    head = llist
    node = llist
    previous = None
    
    # if an empty list is given
    if head is None:
        print('Creating a new linked list')
        return DoublyLinkedListNode(data)
    
    # if the new node should be inserted before head
    if head.data > data:
        print(f'head: {head.data} > data: {data}')
        print('Inserting at the start')
        new_head = DoublyLinkedListNode(data)
        new_head.next = head
        new_head.prev = None
        head.prev     = new_head
        return new_head
    
    # find where the new node should be inserted
    while node is not None and node.data < data:
        previous = node
        node = node.next
        
    # first check if the node is None
    # that means we reached the end of the doubly linked list
    # insert the new node at the end
    if node is None:
        print('Inserting at the end')
        print(f'tail: {previous.data} < data: {data}')
        new_tail = DoublyLinkedListNode(data)
        previous.next = new_tail
        new_tail.prev = previous
        return head
    
    # we are not at the end of the linked list
    # means, we are somewhere between head and before tail
    # now, the current node in variable node
    # has data value greater than the given data value
    # so we can safely insert our new node
    # before this node
    # if we are inserting in between
    print('Inserting in between')
    print(f'after: {node.data} > data: {data}')
    new_node = DoublyLinkedListNode(data)
    new_node.prev       = node.prev
    new_node.prev.next  = new_node
    new_node.next       = node
    node.prev           = new_node
    return head
    
# Kunal Wadhwa
