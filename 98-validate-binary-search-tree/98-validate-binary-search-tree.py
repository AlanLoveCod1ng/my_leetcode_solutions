# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(root,ran):
            mini, maxi = ran
            if not root:
                return True
            inrange = root.val<maxi and root.val>mini
            left = not root.left or root.left.val<root.val
            right = not root.right or root.right.val>root.val
            return inrange and left and right and recursion(root.left,[mini,root.val]) and recursion(root.right,[root.val,maxi])
        return recursion(root,[-math.inf,math.inf])