"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.tail = None
        self.head = None
        self.inorder(root)
        self.tail.right = self.head
        self.head.left = self.tail
        return self.head
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.tail:
            self.tail = root
        else:
            self.tail.right = root
            root.left = self.tail
            self.tail = root
        if not self.head:
            self.head = root
        self.inorder(root.right)