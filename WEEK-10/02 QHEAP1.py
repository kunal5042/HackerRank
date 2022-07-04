import sys
from collections import deque

class MinHeap:
    
    def __init__(self, array = []):
        self.heap = array
        
    def sift_down(self, idx, endidx, heap):
        child_one_idx = 2 * idx + 1
        
        # while there exist child or children of the current node which can be potentially smaller than the current node's value
        while child_one_idx <= endidx:
            ci1 = child_one_idx
            ci2 = child_two_idx = 2 * idx + 2 if 2 * idx + 2 <= endidx else None
               
            # if child 2 exists
            if ci2 is not None:
                if heap[ci1] < heap[ci2]:
                    cmpi = compare_idx = ci1
                else:
                    cmpi = compare_idx = ci2
            else:
            # otherwise compare child 1
                cmpi = ci1    
                
            # if child is smaller than the parent
            if heap[idx] > heap[cmpi]:
                # swap
                heap[idx], heap[cmpi] = heap[cmpi], heap[idx]
                # update the current node
                idx = cmpi
                # update the child one
                child_one_idx = 2 * idx + 1
            else:
            # otherwise we can stop
                break
                
        
    def sift_up(self, idx, heap):
        pidx = parent_idx = (idx - 1) // 2
        
        # while parent exist and parent is greater than the child
        while pidx >= 0:
            if heap[idx] < heap[pidx]:
                # swap
                heap[idx], heap[pidx] = heap[pidx], heap[idx]
                # update the current node
                idx = pidx
                # update the parent
                pidx = (idx - 1) // 2
            else:
                break
                
    
    def insert(self, value, heap):
        # add the value as the last node
        heap.append(value)
        idx = len(heap) - 1
        # shift it up to it's correct position
        self.sift_up(idx, heap)
        
    def remove(self):
        # if heap is not empty
        if len(self.heap) >= 2:
            # swap the root with last node
            self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
            # remove the root after swapping
            to_return = self.heap.pop()
            # shift down the new root to it's correct position
            self.sift_down(0, len(self.heap)-1, self.heap)
            # return the current minimum/root
            return to_return
        else:
            # if only one node in the heap, directly remove it
            if len(self.heap) == 1:
                return self.heap.pop()
                
    def remove_particular_value(self, value):
        # same logic as remove
        if value in self.heap:
            idx = self.heap.index(value)
            self.heap[idx], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[idx]
            to_return = self.heap.pop()
            self.sift_down(idx, len(self.heap)-1, self.heap)
            return to_return
            
                
    def peek(self):
        # root is the minimum value of the heap
        # return it
        if len(self.heap) > 0:
            return self.heap[0]
        
if __name__ == "__main__":
    # process the input
    inputs = deque([int(i) for i in line.strip().split(' ')] for line in sys.stdin)
    # remove the query count
    inputs.popleft()
    
    # create a new MinHeap from my implemenation
    heap = MinHeap()

    # query processing
    while len(inputs) > 0 :
        line = inputs.popleft()
        if line[0] == 1:
            heap.insert(line[1], heap.heap)

        elif line[0] == 2:
            heap.remove_particular_value(line[1])
            
        elif line[0] == 3:
            print(heap.peek())

# Kunal Wadhwa
