class Solution:
    def generate(self, numRows: int) -> List[List[int]]:    
        if numRows <=0:
            return []

        triangle = [[1]]
        for i in range(1,numRows):
            newrow=[1]
            for j in range(1,i):
                newrow.append(triangle[i-1][j-1] + triangle[i-1][j])
            newrow.append(1)
            triangle.append(newrow)
        return triangle

numRows=5
solution= Solution()
ans = solution.generate(numRows)
print(ans)

        
