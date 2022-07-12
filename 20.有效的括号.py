#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mydict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in mydict:
                if len(stack) == 0:
                    return False
                elif stack.pop() != mydict[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0



# @lc code=end

