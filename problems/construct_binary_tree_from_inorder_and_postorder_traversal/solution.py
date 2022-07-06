# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.recursion(postorder,inorder)
    def recursion(self,postorder,inorder):
        if len(postorder) == 0:
            return None
        left_inorder = []
        right_inorder = []
        root = postorder[-1]
        found = False
        for i in range(len(inorder)):
            if inorder[i] == root:
                found = True
                continue
            if not found:
                left_inorder.append(inorder[i])
            else:
                right_inorder.append(inorder[i])
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):len(postorder)-1]
        return TreeNode(root, self.recursion(left_postorder,left_inorder),self.recursion(right_postorder,right_inorder))
        
            