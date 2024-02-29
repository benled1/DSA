import sys
from typing import List
"""
A heap is just a tree which has a method heapify that will reorganize the structure to satisfy 
a given property of the tree. In the case of the max heap, the parent node my be larger than it's children and the tree must be a complete binary tree.
"""

class MaxHeap:

    def __init__(self, size) -> None:
        size: int = 0
        max_size: int = size
        heap: List[int] = []
        heap[0] = sys.maxsize

    def parent(self, pos: int) -> int:
        """
        Return the position of the parent of the element at the input position.
        """
        return pos/2
    
    def left_child(self, pos: int) -> int:
        """
        Return the position of the left child of the element at the input position.
        """
        return 2*pos
    
    def right_child(self, pos: int) -> int:
        """
        Return the position of the right child of the element at the input position.
        """
        return (2*pos) +1
    
    def is_leaf(self, pos: int):
        """
        Return True if the node at the position is a leaf, false otherwise.
        """
        if (pos >= (self.size/2) and pos < self.size):
            return True
        else:
            return False

    def swap(self, pos1: int, pos2:int):
        """
        Swap the positions of the two input nodes in the tree.
        """
        tmp: int = self.heap[pos1]
        self.heap[pos1] = self.heap[pos2]
        self.heap[pos2] = tmp
        return

    def down_heapify(self, pos: int):
        """
        Run down from the root to the leaves ensuring that each parent, child trio satisfies the heap constraints.
        This is done by swapping the parent with a child that is larger, and then calling heapify on the child.
        """
        if (self.is_leaf()):
            return
        
        if (self.heap[pos] < self.heap[self.left_child(pos)] or self.heap[pos] < self.heap[self.right_child(pos)]):
            if (self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]):
                self.swap(pos, self.right_child(pos))
                self.down_heapify(self.right_child(pos))

            elif (self.heap[self.left_child[pos]] > self.heap[self.right_child[pos]]):
                self.swap(pos, self.left_child(pos))
                self.down_heapify(self.left_child(pos))

        


    
    
    
