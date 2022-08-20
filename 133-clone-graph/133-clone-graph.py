"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        root = Node(node.val)
        queue1 = deque([node])
        queue2 = deque([root])
        val_refer = {node.val:root}
        visited = set([])
        while len(queue1) != 0:
            original = queue1.popleft()
            new = queue2.popleft()
            visited.add(original.val)
            neighbors = original.neighbors
            new.neighbors = []
            for i in neighbors:
                refer = val_refer.get(i.val,Node(i.val))
                val_refer[i.val] = refer
                new.neighbors.append(refer)
                if i.val in visited:
                    continue
                queue1.append(i)
                queue2.append(refer)
                
        return root