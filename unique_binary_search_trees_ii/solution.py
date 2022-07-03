# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        result = [[]for _ in range(n+1)]
        result[0].append(None)
        for i in range(1,n+1):
            for j in range(i,0,-1):
                for left in result[j-1]:
                    for right in result[i-j]:
                        result[i].append(TreeNode(j,left,self.nodeClone(right,j)))
        return result[-1]
        
    def nodeClone(self, origin, offset):
        left = None
        right = None
        if origin == None:
            return None
        if origin.right!=None:
            right = self.nodeClone(origin.right, offset)
        if origin.left!=None:
            left = self.nodeClone(origin.left, offset)
        new = TreeNode(origin.val+offset,left,right)
        return new