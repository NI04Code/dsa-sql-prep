from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramDict = defaultdict(list)
        
        for w in strs:
            anagramDict[tuple(sorted(w))].append(w)
        
        result = []
        for val in anagramDict.values():
            result.append(val)
        
        return result
        