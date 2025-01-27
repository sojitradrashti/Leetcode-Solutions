class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        result=[]
        for i in range(len(nums)):
            if (i==0 or nums[i] > nums[i-1]) and (i == len(nums) -1 or nums[i] > nums[i+1]):
                return i
        return -1
                
nums=[1,2,3,1]
solution=Solution()
result=solution.findPeakElement(nums)
print(result)
