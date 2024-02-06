'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = list()

        count_null = strs.count("")
        if count_null > 0:
            ans.append([""]*count_null)
            strs = [e for e in strs if e != '']
            
        
        if len(set(strs)) == 1:
            return [strs]
        
        while strs :
            tmp_list = [strs[0]]
            if strs[1:] :
                for tmp in strs[1:]:
                    if sorted(tmp_list[-1]) == sorted(tmp):
                        tmp_list.append(tmp)
                        print('tmp_list : ', tmp_list)
                        strs.remove(tmp)
            strs.remove(strs[0])
            print('ans : ', ans)
            ans.append(sorted(tmp_list))
            tmp_list = []
        
        return sorted(ans)
