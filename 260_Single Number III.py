class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            
            if nums.count(nums[i])==1 and nums[i] not in result:
                result.append(nums[i])
        return result
nums = [1,2,1,3,2,5]
solution=Solution()
ans = solution.singleNumber(nums)
print(ans)
