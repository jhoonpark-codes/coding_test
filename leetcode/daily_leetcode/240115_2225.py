'''
2225. Find Players With Zero or One Losses

You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

'''

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        ans1 = list()
        ans2 = list()

        count_dict = defaultdict(int)
        players = list()

        for tmp in matches:
            w = tmp[0]
            l = tmp[1]

            players.append(w)
            players.append(l)

            if str(w) + '_win' not in count_dict.keys():
                count_dict[str(w)+'_win'] = 1
            else:
                count_dict[str(w)+'_win'] += 1
            
            if str(l) + '_lose' not in count_dict.keys():
                count_dict[str(l)+'_lose'] = 1
            else:
                count_dict[str(l)+'_lose'] += 1
        
        for player in set(players):
            if count_dict[str(player)+'_lose'] == 0:
                ans1.append(player)
            if count_dict[str(player)+'_lose'] == 1:
                ans2.append(player)
        
        return [sorted(ans1), sorted(ans2)]
