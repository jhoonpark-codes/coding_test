'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        from collections import deque
        ans = 0
        g = deque(g)
        tmp = []
        while g and s :
            tmp_greed = g.popleft()
            tmp = [v if v >= tmp_greed else None for v in s ]
            tmp = list(filter(None, tmp))
            if len(tmp) > 0:
                ans += 1
                s.remove(min(tmp))
            
        
        return and


'''
Best Solution 1
class Solution(object):
    def findContentChildren(self, g, s):
        cookiesNums = len(s)
        if cookiesNums == 0:
            return 0
        g.sort()
        s.sort()

        maxNum = 0
        cookieIndex = cookiesNums - 1
        childIndex = len(g) - 1
        while cookieIndex >= 0 and childIndex >= 0:
            if s[cookieIndex] >= g[childIndex]:
                maxNum += 1
                cookieIndex -= 1
                childIndex -= 1
            else:
                childIndex -= 1

        return maxNum
'''

'''
Best Solution 2
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        it = iter(sorted(s))
        return sum(any(gi <= si for si in it) for gi in sorted(g))

'''




