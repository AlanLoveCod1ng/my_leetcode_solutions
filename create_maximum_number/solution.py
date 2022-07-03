class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        maximum = [0]*k
        for i in range(k+1):
            if i > len(nums1) or k-i > len(nums2):
                continue
            array1 = self.getSubsequence(nums1,i)
            array2 = self.getSubsequence(nums2,k-i)
            result = []

            # while pointer1 < i or pointer2< k-i:
            #     if pointer1 == i:
            #         result.append(array2[pointer2])
            #         pointer2+=1
            #         continue
            #     if pointer2 == k-i:
            #         result.append(array1[pointer1])
            #         pointer1+=1
            #         continue
            #     if array1[pointer1] > array2[pointer2]:
            #         result.append(array1[pointer1])
            #         pointer1+=1
            #     else:
            #         result.append(array2[pointer2])
            #         pointer2+=1
            result = self.mergeMax(array1,array2)
            maximum = self.maxListDigit(result,maximum)
        return maximum
            
    def getSubsequence(self, nums, k):
        stack = []
        for i in range(len(nums)):
            if len(stack) == 0:
                stack.append(nums[i])
                continue
            while len(stack)!=0:
                if stack[-1] < nums[i] and len(stack)+len(nums)-i-1>=k:
                    stack.pop()
                    if len(stack) == 0:
                        stack.append(nums[i])
                        break
                else:
                    stack.append(nums[i])
                    break
        result = []
        for i in range(k):
            result.append(stack[i])
        return result
    def maxListDigit(self, list1,list2):
        for i in range(len(list1)):
            if list1[i]>list2[i]:
                return list1
            elif list1[i]<list2[i]:
                return list2
            else:
                continue
        return list1
    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        return ans