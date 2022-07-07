#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
from re import L


class Solution:
    def longestCommonPrefix(self, strs):
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix
                
# @lc code=end

