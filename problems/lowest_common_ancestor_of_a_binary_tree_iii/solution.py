"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = []
        q_ancestors = []
        while p != None:
            if p == q:
                return q
            p_ancestors.append(p)
            p = p.parent           
        while q !=None:
            if p == q:
                return p
            q_ancestors.append(q)
            q = q.parent
        p_ancestors.reverse()
        q_ancestors.reverse()
        index = 0
        while index < len(p_ancestors) and index<len(q_ancestors) and p_ancestors[index] == q_ancestors[index]:
            index+=1
        return p_ancestors[index-1]