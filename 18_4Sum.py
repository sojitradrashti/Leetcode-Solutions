class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=set()
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(b+1,len(nums)):
                    for d in range(c+1,len(nums)):
                        if nums[a]+ nums[b]+ nums[c]+ nums[d] == target:
                            list1=[nums[a],nums[b],nums[c],nums[d]]
                            result.add(tuple(list1))    
        return list(result)
nums=[1,0,-1,0,-2,2]
target=0
r=Solution()
x= r.fourSum(nums,target)
print(x)
