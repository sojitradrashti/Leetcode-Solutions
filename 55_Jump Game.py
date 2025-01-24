class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i > maxJump:
                    return False
                maxJump=max(maxJump,i+nums[i])

                if maxJump >= len(nums)-1:
                    return True
        return True
nums=[2,3,1,1,4]
solution=Solution()
result=solution.canJump(nums)
print(result)
