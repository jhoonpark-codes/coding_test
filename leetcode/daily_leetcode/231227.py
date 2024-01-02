# 1578. Minimum Time to Make Rope Colorful

'''
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.
'''

'''
Beats 82.83%of users with Python3
Beats 8.18%of users with Python3
'''

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        from collections import deque
        color_list = list(colors)
        color_que = deque(color_list)

        idx = 1
        ans = 0
        tmp = color_que.popleft()
        needed_candidate = [neededTime[0]]
        while idx < len(color_list):
            tmp_next = color_que.popleft() 
            if tmp==tmp_next:
                needed_candidate.append(neededTime[idx])
                tmp = tmp_next
                if idx == len(color_list) -1 :
                    srtd = sorted(needed_candidate)
                    ans += sum(srtd[:-1])

            else:
                if len(needed_candidate) > 1:
                    srtd = sorted(needed_candidate)
                    ans += sum(srtd[:-1])
                    needed_candidate = [neededTime[idx]]
                else:
                    tmp = tmp_next
                    needed_candidate = [neededTime[idx]]

            tmp = tmp_next
            idx += 1
        
        return ans
