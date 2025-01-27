class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        list1=[1]
        prev=1
        for i in range(1,rowIndex+1):
            nextValue = prev * (rowIndex- i + 1)//i
            list1.append(nextValue)
            prev = nextValue
        return list1
rowIndex = 3
solution = Solution()
result = solution.getRow(rowIndex)
print(result)
        
