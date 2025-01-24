class Solution:
    def findMin(self, nums: List[int]) -> int:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] >= nums[j]:
                    nums.append(result)
                else:
                    return nums[i]
        return nums[i]
nums=[3,4,5,1,2]
solution= Solution()
ans = solution.findMin(nums)
print(ans)                   

