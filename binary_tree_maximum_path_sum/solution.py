# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxValue = float('-inf')
        self.traverse(root)
        return self.maxValue
    def traverse(self,node):
        leftValue = 0
        rightValue = 0
        if node.left != None:
            leftValue = self.traverse(node.left)
        if node.right != None:
            rightValue = self.traverse(node.right)
        self.maxValue = max(self.maxValue,max(rightValue,0)+max(leftValue,0)+node.val)
        node.val += max(rightValue,leftValue,0)
        return node.val
        