# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        self.recusion(root)
        return self.valid
    def recusion(self,current):
        left = []
        right = []
        valid = True
        maxi = current.val
        mini = current.val
        if current.left:
            left = self.recusion(current.left)
        if current.right:
            right = self.recusion(current.right)
        if len(left) != 0:
            valid = valid and current.val > left[1]
            mini = left[0]
        if len(right) != 0:
            valid = valid and current.val < right[0]
            maxi = right[1]
        self.valid = self.valid and valid
        return [mini,maxi]