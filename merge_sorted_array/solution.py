class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = [0]*(m+n)
        mIndex = 0
        nIndex = 0
        rIndex = 0
        while True:
            if n==nIndex and m==mIndex:
                break
            if n==nIndex:
                result[rIndex] = nums1[mIndex]
                mIndex+=1
                rIndex+=1
                continue
            if m==mIndex:
                result[rIndex] = nums2[nIndex]
                nIndex+=1
                rIndex+=1
                continue
            if nums1[mIndex]<nums2[nIndex]:
                result[rIndex] = nums1[mIndex]
                rIndex+=1
                mIndex+=1
            elif nums1[mIndex]>nums2[nIndex]:
                result[rIndex] = nums2[nIndex]
                nIndex+=1
                rIndex+=1
            else:
                result[rIndex] = nums1[mIndex]
                mIndex+=1
                rIndex+=1
        for i in range(len(nums1)):
            nums1[i] = result[i]