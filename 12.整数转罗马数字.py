#
# @lc app=leetcode.cn id=12 lang=python
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        table       = [1000,    900,    500,    400,    100,    90,     50,     40,     10,     9,      5,      4,      1]
        unit   = ['M',     'CM',   'D',    'CD',   'C',    'XC',   'L',    'XL',   'X',    'IX',   'V',    'IV',   'I']
        i = 0
        res = ""
        while num > 0:
            while num < table[i]:
                i += 1
            num -= table[i]
            res += unit[i]
        return res

# @lc code=end

