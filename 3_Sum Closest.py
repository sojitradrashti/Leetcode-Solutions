class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        cl_sum=float('inf')
        for a in range(len(nums)-2):
            for b in range(a+1,len(nums)-1):
                for c in range(b+1,len(nums)):
                    ans=nums[a]+nums[b]+nums[c]
                    if abs(ans-target) < abs(cl_sum-target):
                        cl_sum=ans
                    if ans==target:
                        return ans
        return cl_sum
                    
nums=[-1,2,1,-4]
target=1
solution=Solution()
x=solution.threeSumClosest(nums,target)
print(x)
