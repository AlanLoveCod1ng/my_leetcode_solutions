# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.p_path = []
        self.q_path = []
        self.inorder(root,[])
        index = 0
        while index < len(self.p_path) and index < len(self.q_path) and self.p_path[index] == self.q_path[index]:
            index+=1
        return self.p_path[index-1]
        
    def inorder(self,root,path):
        if not root:
            return
        newPath = path+[root]
        if root == self.p:
            self.p_path = newPath
        if root == self.q:
            self.q_path = newPath
        self.inorder(root.left,newPath)
        self.inorder(root.right,newPath)
        
        
        