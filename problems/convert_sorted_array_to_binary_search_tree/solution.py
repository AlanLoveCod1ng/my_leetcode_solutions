# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.recursion(nums)
    def recursion(self, nums):
        if len(nums) == 0:
            return None
        middleIndex = int(len(nums)/2)
        return TreeNode(nums[middleIndex], self.recursion(nums[:middleIndex]),self.recursion(nums[middleIndex+1:]))
        