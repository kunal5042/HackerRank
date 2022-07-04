#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def sorted_insert(llist, data):
    # if the given llist is empty
    head = llist
    node = llist
    
    if head is None: return SinglyLinkedListNode(data)

    # if new node should be inserted at the start
    if data < head.data:
        new_head = SinglyLinkedListNode(data)
        new_head.next = head
        return new_head
    
    # find the sorted position
    previous = node
    while node is not None and data > node.data:
        previous = node
        node = node.next
        
    # check if we reached the end of the llist
    if node is None:
        # insert the new node at the tail
        new_node = SinglyLinkedListNode(data)
        previous.next = new_node
        new_node.next = None
        return head
    
    # current node.data is > than data
    # insert new node before the current node
    new_node = SinglyLinkedListNode(data)
    previous.next = new_node
    new_node.next = node
    return head
    
def mergeLists_time_limit_exceeded(head1, head2):
    merged_list_head = head1
    
    head_of_list_to_insert_from = head2
    previous_of_head = None
    
    # traverse till the end
    while head_of_list_to_insert_from is not None:
        previous_of_head = head_of_list_to_insert_from
        head_of_list_to_insert_from = head_of_list_to_insert_from.next
        
        # insert the data of previous of head
        merged_list_head = sorted_insert(merged_list_head, previous_of_head.data)
        
    return merged_list_head
    
    
def mergeLists(head1, head2):
    combined_values_both_lists = []
    merged_list_head = None

    while head1 is not None:
        combined_values_both_lists.append(head1.data)
        head1 = head1.next
        
    while head2 is not None:
        combined_values_both_lists.append(head2.data)
        head2 = head2.next
        
    combined_values_both_lists.sort()

    merged_list_head = SinglyLinkedListNode(combined_values_both_lists[0])
    node = merged_list_head
    
    for idx in range(1, len(combined_values_both_lists)):
        new_node = SinglyLinkedListNode(combined_values_both_lists[idx])
        node.next = new_node
        node = node.next
        
    return merged_list_head
            
# Kunal Wadhwa
