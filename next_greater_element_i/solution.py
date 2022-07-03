class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unassigned = []
        assigned = {}
        for i in nums2:
            while len(unassigned)!=0:
                j = unassigned[-1]
                if j < i:
                    assigned[j] = i
                    unassigned.pop()
                else:
                    break
            unassigned.append(i)
        for i in unassigned:
            assigned[i] = -1
        result = []
        for i in nums1:
            result.append(assigned[i])
        return result