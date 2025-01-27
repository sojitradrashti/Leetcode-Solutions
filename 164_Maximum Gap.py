class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxgap=0
        for i in range(1,len(nums)):
            maxgap=max(maxgap,nums[i]-nums[i-1])
        return maxgap
nums=[3.6,9,1]        
