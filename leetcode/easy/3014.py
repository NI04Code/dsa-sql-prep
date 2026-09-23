# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        word_counts = Counter(word).most_common()

        total_key_pushed = 0
        for i in range(len(word_counts)):
            total_key_pushed += word_counts[i][1] * ((i // 8) + 1)
        
        return total_key_pushed