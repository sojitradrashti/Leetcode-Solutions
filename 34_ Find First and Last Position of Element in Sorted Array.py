class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[]
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if target == nums[i]:
                result.append(i)
                break
        for i in range(-1,-len(nums),-1):
            if target == nums[i]:
                result.append(len(nums)+i)
                break
        return [result[0],result[-1]]
nums = [5, 7, 7, 8, 8, 10]
target = 8
solution = Solution()
ans = solution.searchRange(nums, target)
print(ans)
