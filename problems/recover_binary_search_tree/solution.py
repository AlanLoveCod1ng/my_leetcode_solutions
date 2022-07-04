# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.array = []
        array = self.array
        self.recusion(root)
        invalid = []
        for i in range(len(self.array)-1):
            if self.array[i].val>self.array[i+1].val: 
                temp = self.array[i+1].val
                self.array[i+1].val = self.array[i].val
                self.array[i].val = temp
        for i in range(len(self.array)-1,0,-1):
            if self.array[i].val<self.array[i-1].val: 
                temp = self.array[i-1].val
                self.array[i-1].val = self.array[i].val
                self.array[i].val = temp
        
    def recusion(self, root):
        if not root:
            return
        self.recusion(root.left)
        self.array.append(root)
        self.recusion(root.right)