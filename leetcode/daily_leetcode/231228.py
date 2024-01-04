'''
1531. String Compression II

Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.

 

Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
'''

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def run_length_encoding(s:str):
            cnt = 0
            cur = ''
            for i in range(len(list(s))-1):
                tmp, tmp_next = list(s)[i], list(s)[i+1]
                if tmp == tmp_next:
                    cnt+=1
                else:
                    if cnt != 0:
                        cur+=tmp
                        cur+=str(cnt+1)
                        cnt = 0
                    else:
                        cur += tmp
            cur+=s[-1]
            return cur

        from collections import Counter
        s_list = list(s)
        s_counter = Counter(s_list)

        while k:
            for i in range(len(s_list)):
                if 

        return 1
        
