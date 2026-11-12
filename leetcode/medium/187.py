class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        n = len(s)
        if n <= 10:
            return []

        seen = set()
        duplicate = set()
        i = 0; j = 10
        while j <= n:
            seq = s[i:j]
            if seq in seen:
                duplicate.add(seq)
            
            seen.add(seq)
            i += 1
            j += 1
        
        return list(duplicate)