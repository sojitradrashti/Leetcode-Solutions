class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count+=1
            else:
                count=1
            if count > len(nums)//2:
                return nums[i]
        return nums[0]
          

       
nums=[3,2,3]
        
