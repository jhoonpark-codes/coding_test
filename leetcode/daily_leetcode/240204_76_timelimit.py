'''
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t_counter = Counter(list(t))
        ans = 'A' * 10**5
            
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                tmp_s = s[i:j]

                # if (len(set(list(t_counter.keys())) - set(list(tmp_s))) == 0) & len(set(list(tmp_s))) >0:
                is_contain = True
                for key, value in t_counter.items():
                    if (key in list(tmp_s)) & (tmp_s.count(key) >= value):
                        continue
                    else:
                        is_contain = False
                if is_contain:
                    # print('tmp_s : ', tmp_s)
                    # print('i,j : ',i, ' ,', j)
                    if len(ans) > len(tmp_s):
                        ans = tmp_s

        if ans == 'A' * 10**5 :
            return ''
        else:
            return ans
