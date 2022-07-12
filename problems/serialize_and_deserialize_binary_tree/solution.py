# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result_list = []
        if not root:
            return "None"
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current:
                result_list.append(str(current.val))
                queue.append(current.left)
                queue.append(current.right)
            else:
                result_list.append('None')
        return " ".join(result_list)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_list = data.split(" ")
        if node_list[0] == 'None':
            return None
        root = TreeNode(int(node_list[0]))
        queue = deque([root])
        current_index = 1
        while queue:
            current = queue.popleft()
            if current_index<len(node_list):
                leftChild = None if node_list[current_index] == 'None' else TreeNode(int(node_list[current_index]))
                current.left = leftChild
                current_index+=1
                if leftChild:
                    queue.append(leftChild)
            else:
                break
            if current_index<len(node_list):
                rightChild = None if node_list[current_index] == 'None' else TreeNode(int(node_list[current_index]))
                current.right = rightChild
                current_index+=1
                if rightChild:
                    queue.append(rightChild)
            else:
                break
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))