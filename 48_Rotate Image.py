class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp=0
        matrix.reverse()
        for index in range(len(matrix)):
            for column in range(index+1,len(matrix)):
                temp= matrix[index][column]
                matrix[index][column] = matrix[column][index]
                matrix[column][index] = temp
        return matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]
solution=Solution()
result=solution.rotate(matrix)
print(result)
