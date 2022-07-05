# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True
        self.recusion(p,q)
        return self.result
    def recusion(self, root1, root2):
        identical = False
        if root1 == None and root2 == None:
            identical = True
            return
        elif root1 and root2:
            if root1.val == root2.val:
                identical = True
        self.result = self.result and identical
        if not identical:
            return
        self.recusion(root1.left,root2.left)
        self.recusion(root1.right,root2.right)
        