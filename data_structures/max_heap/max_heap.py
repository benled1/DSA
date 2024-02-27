import sys
from typing import List


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
        return self.heap[pos/2]
    
    def left_child(self, pos: int) -> int:
        """
        Return the position of the left child of the element at the input position.
        """
        return self.heap[2*pos]
    
    def right_child(self, pos: int) -> int:
        """
        Return the position of the right child of the element at the input position.
        """
        return self.heap[(2*pos)+1]
    
    
