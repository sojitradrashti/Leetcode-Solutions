class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp=0
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                temp= matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        return matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]
solution=Solution()
result=solution.rotate(matrix)
print(result)
