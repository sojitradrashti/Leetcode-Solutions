class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        return -1
nums=[1,3,4,2,2]
solution=Solution()
ans = solution.findDuplicate(nums)
print(ans)
