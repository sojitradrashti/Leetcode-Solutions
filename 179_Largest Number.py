class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(0,len(nums)-1-i):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j] ,nums[j+1] = nums[j+1],nums[j]
        list1 = list(map(str, nums))
        result=''.join(list1)
        if nums[0] == 0:
            return "0"
        return result      
nums=[10,2]
solution= Solution()
ans = solution.largestNumber(nums)
print(ans)
