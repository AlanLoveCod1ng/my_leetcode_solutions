class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashtable = {}
        maxScore = 0
        currentScore = 0
        startIndex = 0
        endIndex = 0
        while endIndex<len(nums):
            if nums[endIndex] in hashtable:
                prevIndex = hashtable[nums[endIndex]]
                while startIndex<prevIndex+1:
                    currentScore -= nums[startIndex]
                    hashtable.pop(nums[startIndex],None)
                    startIndex+=1
            hashtable[nums[endIndex]] = endIndex
            currentScore+=nums[endIndex]
            endIndex+=1
            maxScore = max(maxScore, currentScore)
        return maxScore