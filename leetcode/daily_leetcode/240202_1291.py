'''
1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
'''

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_len  = len(str(low))
        high_len = len(str(high))
        ans = list()

        tmp = '0'
        for i in range(low_len, high_len+1):
            for j in range(1, 10):
                tmp = str(j)
                for k in range(1, i):
                    if int(str(j))+k < 10 :
                        tmp += str(int(str(j))+k)
                print('tmp : ', int(tmp))
                
                if (low <= int(tmp)) and (int(tmp) <= high):
                    ans.append(int(tmp))
                    tmp = ''
        
        return sorted(set(ans))

