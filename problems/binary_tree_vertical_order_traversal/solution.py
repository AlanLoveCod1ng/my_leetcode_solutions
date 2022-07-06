# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        hashtable = {}
        min1 = 0
        max1 = 0
        result = []
        queue1 = deque([root])
        queue2 = deque([0])
        while len(queue1) != 0:
            current_node = queue1.popleft()
            current_index = queue2.popleft()
            temp = hashtable.get(current_index,[])
            temp.append(current_node.val)
            min1 = min(current_index,min1)
            max1 = max(current_index,max1)
            hashtable[current_index] = temp
            if current_node.left:
                queue1.append(current_node.left)
                queue2.append(current_index-1)
            if current_node.right:
                queue1.append(current_node.right)
                queue2.append(current_index+1)
        for i in range(min1,max1+1):
            result.append(hashtable[i])
        return result