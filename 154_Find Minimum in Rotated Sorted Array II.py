class Solution:
    def findMin(self, nums: List[int]) -> int:
        result=set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] >= nums[j]:
                    nums.extend(result)
                else:
                    return nums[i]
        return nums[i]
nums=[2,2,2,0,1]
solution= Solution()
ans = solution.findMin(nums)
print(ans)         
        
