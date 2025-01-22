class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        m=n/2
        if n % 2 == 0:
            ans = (nums1[int(m)-1] + nums1[int(m)]) / 2 
        else:
            ans = nums1[int(m)]
        return ans

nums1=[1,3]
nums2=[2]
result=Solution()
x = result.findMedianSortedArrays(nums1,nums2)
print(x)
