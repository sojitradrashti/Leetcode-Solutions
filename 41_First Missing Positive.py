class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=[n for n in nums if n > 0]
        nums.sort()
        target=1

        for i in range(len(nums)):
            if nums[i] == target:
                target+=1
            if nums[i] > target:
                return target
        return target

nums=[1,2,0]
solution=Solution()
result=solution.firstMissingPositive(nums)
print(result)
