class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num={}
        i=0
        while i< len(numbers):
            ans = target-numbers[i]
            if ans in num:
                return [num[ans] + 1,i+1]
            num[numbers[i]] = i
            i+=1
numbers=[2,7,11,15]
target=9
result=Solution()
x=result.twoSum(numbers,target)
print(x)
        
