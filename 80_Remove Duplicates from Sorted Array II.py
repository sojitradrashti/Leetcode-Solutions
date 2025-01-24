class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        k=0
        for i in range(len(nums)):
            if nums[i]== nums[i-1]:
                j+=1    
            else:
                j=1
            if j<=2:
                nums[k] = nums[i]
                k+=1
        return k       
nums=[1,1,1,2,2,3]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)

        
