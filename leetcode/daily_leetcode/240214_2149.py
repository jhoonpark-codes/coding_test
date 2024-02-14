class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # from collections import deque
        # tmp = deque(list())
        pos_list = list()
        neg_list = list()

        ans = list()

        for tmp in nums:
            if tmp > 0 : 
                pos_list.append(tmp)
            else:
                neg_list.append(tmp)
        
        for i in range(len(pos_list)):
            ans.append(pos_list[i])
            ans.append(neg_list[i])
        
        return ans
