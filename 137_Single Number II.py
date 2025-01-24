class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=None
        for i in range(len(nums)):
            result1=nums.count(nums[i])
            if result1 == 1:
                result=nums[i]
        return result
nums = [2,2,3,2]
solution=Solution()
ans = solution.singleNumber(nums)
print(ans)
