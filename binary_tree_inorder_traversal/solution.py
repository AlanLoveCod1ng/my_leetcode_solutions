# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# recusion
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         self.result = []
#         self.inorder(root)
#         return self.result
#     def inorder(self, parent):
#         if parent == None:
#             return
#         self.inorder(parent.left)
#         self.result.append(parent.val)
#         self.inorder(parent.right)
# iteration
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while root:
            stack.append(root)
            root = root.left
        while len(stack) != 0:
            current = stack.pop()
            result.append(current.val)
            current = current.right
            while current:
                stack.append(current)
                current = current.left
        return result
            