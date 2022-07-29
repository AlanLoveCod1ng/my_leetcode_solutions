# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preorder(root,None)
        return root
    def preorder(self,root,prev):
        if root == None:
            return
        leftChild = root.left
        rightChild = root.right
        if prev!=None:
            prev.right = root
            prev.left= None
        left_tail = self.preorder(leftChild,root)
        right_tail = self.preorder(rightChild,left_tail)
        if right_tail != None:
            return right_tail
        elif left_tail != None:
            return left_tail
        else:
            return root