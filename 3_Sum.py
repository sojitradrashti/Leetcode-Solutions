class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+ nums[j]+ nums[k] == 0:
                        list1=[nums[i],nums[j],nums[k]]
                        result.add(tuple(list1))    
        return list(result)
nums=[-1,0,1,2,-1,-4]
r=Solution()
x= r.threeSum(nums)
print(x)
