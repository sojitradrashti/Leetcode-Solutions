class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        nums=list(set(nums))
        nums.sort()
        target=0

        for i in range(len(nums)):
            if nums[i] == target:
                target+=1
            if nums[i] > target:
                return target
        return target

nums=[3,0,1]
solution=Solution()
result=solution.missingNumber(nums)
print(result)
