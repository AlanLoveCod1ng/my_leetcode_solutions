"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current
        else:
            current = node.parent
            while current:
                if current.val>node.val:
                    return current
                else:
                    current = current.parent
        return None