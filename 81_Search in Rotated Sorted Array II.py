class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False
nums=[2,5,6,0,0,1,2]
target=0
solution= Solution()
result= solution.search(nums,target)
print(target)


        
