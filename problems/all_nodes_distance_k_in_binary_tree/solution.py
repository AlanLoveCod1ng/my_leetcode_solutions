# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.hashtable = {}
        self.traverse(root,None)
        stack1 = [target]
        stack2 = []
        visited = set([])
        current_distance = 0
        while stack1:
            if current_distance == k:
                break
            while stack1:
                current_node = stack1.pop()
                visited.add(current_node)
                if current_node.left and not current_node.left in visited:
                    stack2.append(current_node.left)
                if current_node.right and not current_node.right in visited:
                    stack2.append(current_node.right)
                if self.hashtable[current_node] and not self.hashtable[current_node] in visited:
                    stack2.append(self.hashtable[current_node])
            current_distance+=1
            stack1 = stack2
            stack2 = []
        result = [node.val for node in stack1]
        return result
        
    def traverse(self, current_node,parent):
            if current_node == None:
                return
            self.hashtable[current_node] = parent
            self.traverse(current_node.left,current_node)
            self.traverse(current_node.right,current_node)