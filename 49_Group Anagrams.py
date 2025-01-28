class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for i in strs:
            key=''.join(sorted(i))
            result[key].append(i)

        return list(result.values())
strs = ["eat","tea","tan","ate","nat","bat"]
solution=Solution()
ans = solution.groupAnagrams(strs)
print(ans)


            
