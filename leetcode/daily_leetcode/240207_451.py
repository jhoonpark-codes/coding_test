class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        s_counter = Counter(list(s))

        s_counter_sorted = {key : value for key, value in sorted(s_counter.items(), key = lambda item: item[1])}

        ans = ''

        for key, value in s_counter_sorted.items():
            ans += key * value
        
        return ans[::-1]
