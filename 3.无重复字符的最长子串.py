#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        memDict = {}
        start = -1
        maxLen = 0
        for i in range(len(s)):
            lastIdx = memDict.get(s[i])
            if not (lastIdx == None or lastIdx <= start):
                start = lastIdx
            curLen = i - start
            maxLen = max(curLen, maxLen)
            memDict[s[i]] = i
        return maxLen


# @lc code=end

