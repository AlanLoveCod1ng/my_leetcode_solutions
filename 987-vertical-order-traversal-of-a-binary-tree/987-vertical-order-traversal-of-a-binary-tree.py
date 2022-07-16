# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashtable = {}
        queue1_node = deque([root])
        queue2_node = deque([])
        queue1_index = deque([0])
        queue2_index = deque([])
        min_index = 0
        max_index = 0
        while queue1_node:
            current_hashtable = {}
            while queue1_node:
                current_node = queue1_node.popleft()
                current_index = queue1_index.popleft()
                min_index = min(min_index,current_index)
                max_index = max(max_index,current_index)
                temp_list = current_hashtable.get(current_index,[])
                temp_list.append(current_node.val)
                current_hashtable[current_index] = temp_list
                if current_node.left:
                    queue2_node.append(current_node.left)
                    queue2_index.append(current_index-1)
                if current_node.right:
                    queue2_node.append(current_node.right)
                    queue2_index.append(current_index+1)
            queue1_node = queue2_node
            queue1_index = queue2_index
            queue2_node = deque([])
            queue2_index = deque([])
            for i in current_hashtable:
                current = current_hashtable[i]
                current = sorted(current)
                total = hashtable.get(i,[])
                hashtable[i] = total+current
        result = []
        for i in range(min_index, max_index+1):
            result.append(hashtable[i])
        return result