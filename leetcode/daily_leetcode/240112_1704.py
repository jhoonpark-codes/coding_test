'''
1704. Determine if String Halves Are Alike
BEAT Beats 83.40% of users with Python3

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        from collections import Counter
        s = s.lower()
        vowels= ['a', 'e', 'i', 'o', 'u']

        l1 = list(s[0:len(s)//2])
        l2 = list(s[len(s)//2:])

        l1_counter = Counter(l1)
        l2_counter = Counter(l2)

        ans1 = 0
        ans2 = 0

        for v in vowels:
            if v in l1_counter.keys():
                ans1 += l1_counter[v]
            if v in l2_counter.keys():
                ans2 += l2_counter[v]
        
        if ans1 == ans2 :
            return True
        else:
            return False
