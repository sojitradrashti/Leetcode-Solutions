class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pivot1=m-1
        pivot2=n-1
        pivot= m+n-1

        while pivot2 >= 0:
            if pivot1 >= 0 and nums1[pivot1] > nums2[pivot2]:
                nums1[pivot] = nums1[pivot1]
                pivot1-=1
            else:
                nums1[pivot] = nums2[pivot2]
                pivot2-=1
            pivot-=1
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=2
solution=Solution()
ans = solution.merge(nums1,m,nums2,n)
print(ans)
        
