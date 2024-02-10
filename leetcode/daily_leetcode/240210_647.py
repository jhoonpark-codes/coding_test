'''
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.


'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = list()
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                tmp = s[i:j]
                if tmp == tmp[::-1]:
                    ans.append(tmp)
        
        return len(ans)
