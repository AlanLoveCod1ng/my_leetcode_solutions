# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.recursion(preorder,inorder)
    def recursion(self,preorder,inorder):
        if len(preorder) == 0:
            return None
        left_inorder = []
        right_inorder = []
        root = preorder[0]
        found = False
        for i in range(len(inorder)):
            if inorder[i] == root:
                found = True
                continue
            if not found:
                left_inorder.append(inorder[i])
            else:
                right_inorder.append(inorder[i])
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        return TreeNode(root, self.recursion(left_preorder,left_inorder),self.recursion(right_preorder,right_inorder))
        
            