class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct = minproduct= result= nums[0]
        for i in range(1,len(nums)):
            current=nums[i]
            if current < 0:
                maxproduct,minproduct = minproduct,maxproduct
            maxproduct = max(current,maxproduct*current)
            minproduct = min(current,minproduct*current)
            result = max(result,maxproduct)
        return result
nums=[2,3,-2,4]
        
