#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#
# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s))]
        res = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2
                    if i-2>=0:
                        dp[i] += dp[i-2]

                elif dp[i-1]>0 and ( i-dp[i-1]-1 >=0 ) and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1]+2
                    if i-dp[i-1]-2>=0:
                        dp[i] += dp[i-dp[i-1]-2]
                res = max(res, dp[i])

        return res

# @lc code=end

# res = Solution().longestValidParentheses("()(()(()))")
# print(res)


# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         startMap = [-1 for x in xrange(len(s))]
#         res = 0
#         i = 0
#         while i < len(s)-1:
#             if s[i] == '(' and s[i+1] == ')':
#                 # dp[i][i+1] = True
#                 startMap[i+1] = i
#                 l = i-1
#                 r = i+2
#                 while True:
#                     prevL = l
#                     while l >= 0 and r < len(s) and s[l] == '(' and s[r] == ')': # 中心扩展
#                         # dp[l][r] = True
#                         startMap[r] = l
#                         l -= 1
#                         r += 1
#                     r -= 1 # ..((()))..右边界
#                     while l >= 0 and startMap[l] > -1: # 向左合并区间
#                         # dp[startMap[l]][r] = True
#                         startMap[r] = startMap[l]
#                         l = startMap[l] - 1
#                     r += 1
#                     if prevL == l:
#                         i = r-1
#                         break
#                 res = max(r-l-1, res)
#             i += 1
#         return res