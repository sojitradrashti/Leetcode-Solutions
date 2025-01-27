class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle1=triangle[-1][:]
        for i in range(len(triangle) - 2,-1,-1):
            for j in range(i+1):
                triangle1[j] = triangle [i][j] + min(triangle1[j],triangle1[j+1])
                
        return triangle1[0]
triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
solution= Solution()
ans = solution.minimumTotal(triangle)
print(ans)


