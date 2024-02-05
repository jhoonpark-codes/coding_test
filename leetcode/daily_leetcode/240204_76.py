class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t_counter = Counter(list(t))
        ans = 'A' * 10**5
            
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                tmp_s = s[i:j]

                if (len(set(list(t_counter.keys())) - set(list(tmp_s))) == 0) & len(set(list(tmp_s))) >0:
                    print('tmp_s : ', tmp_s)
                    print('i,j : ',i, ' ,', j)
                    if len(ans) > len(tmp_s):
                        ans = tmp_s

        if ans == 'A' * 10**5 :
            return ''
        else:
            return ans
