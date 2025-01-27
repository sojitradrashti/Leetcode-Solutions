class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary={}
        for i in range(len(nums)):
            if nums[i] in dictionary and abs(i-dictionary[nums[i]]) <= k:
                return True
            dictionary[nums[i]] = i
        return False
    
nums = [1,0,1,1]
k = 1
solution=Solution()
result=solution.containsNearbyDuplicate(nums,k)
print(result)
