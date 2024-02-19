'''
231. Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        else:
            while n > 1:
                if n % 2 != 0:
                    return False
                else:
                    n = n//2
        return True


'''
Solution 1 -> make all possible answer using loop
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            ans = 2 ** i
            if ans == n:
                return True
        return Fals

'''

'''
BEST!
return n > 0 and (n & (n - 1)) == 0

'''
