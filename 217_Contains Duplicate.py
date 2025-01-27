class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False
nums = [1,2,3,1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)
