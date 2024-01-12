'''

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1

'''
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        counter_dict = Counter(arr)
        arr_len = len(arr)
        ans = list()

        for key, value in counter_dict.items() :
            if value / arr_len >= 0.25:
                ans.append(key)
            else:pass
        
        return(max(ans))
