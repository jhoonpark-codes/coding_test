'''

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
[[1, 0, 0],
 [0, 0, 1],
 [1, 0, 0]]

Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
'''
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = []
        from collections import Counter
        for i in range(len(mat)):
            if Counter(mat[i])[1] == 1:
                print('i : ', i)
                idx = mat[i].index(1)
                print('idx : ', idx)
                cols = list()
                for col in mat:
                    cols.append(col[idx])
                if Counter(cols)[1] == 1:
                    ans.append([i, idx])
        
        return len(ans)
