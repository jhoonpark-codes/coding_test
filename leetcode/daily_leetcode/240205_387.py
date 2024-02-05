class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        s_counter = Counter(list(s))
        ans = -1
        for key, value in s_counter.items():
            if value == 1:
                return list(s).index(key)
        
        return ans
