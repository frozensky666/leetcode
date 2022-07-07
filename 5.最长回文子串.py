#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start


# class Solution(object): # dp
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         sLen = len(s)
#         dp = [
#             [ False for j in range(sLen) ]
#             for i in range(sLen)
#         ]
#         resTuple = [0,0]
#         for j in range(sLen): # 注意dp计算方向
#             for i in range(0, j+1):
#                 if i == j:
#                     dp[i][j] = True
#                 elif i+1 == j and s[i] == s[j]:
#                     dp[i][j] = True
#                 elif dp[i+1][j-1] and s[i] == s[j]:
#                     dp[i][j] = True
#                 if dp[i][j] and j-i>resTuple[1]-resTuple[0]:
#                     resTuple[0] = i
#                     resTuple[1] = j
#         return s[resTuple[0]:resTuple[1]+1]



class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

# @lc code=end

# zxks


# dp
# dp[i][j] = true if i == j
# dp[i][j] = true if i+1 == j and s[i] == s[j]
# dp[i][j] = true if dp[i+1][j-1] and s[i] == s[j]
# else dp[i][j] = false


