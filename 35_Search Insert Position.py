class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
         for i in range(len(nums)):
            if (nums[i] == target):
                return i
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)
nums=[1,3,5,6]
target= 5
result = Solution()
x = result.searchInsert(nums,target)
print(x)
