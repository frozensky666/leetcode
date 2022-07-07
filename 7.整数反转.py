#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = "2147483647"
        MINUS_MAX = "2147483648"
        MAX_NUM = 2147483647
        MINUS_MAX_NUM = -2147483648

        if x == MINUS_MAX_NUM:
            return 0
        
        positive = True
        if x < 0:
            positive = False
            x = -x
        x = str(x)[::-1]
        if positive:
            if len(x) >= len(MAX) and x > MAX:
                return 0
            return int(x)
        else:
            if len(x) >= len(MINUS_MAX) and x > MINUS_MAX:
                return 0
            return -int(x)

        

# @lc code=end

