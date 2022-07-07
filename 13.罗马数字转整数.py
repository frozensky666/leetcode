#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table       = [1000,    900,    500,    400,    100,    90,     50,     40,     10,     9,      5,      4,      1]
        unit   = ['M',     'CM',   'D',    'CD',   'C',    'XC',   'L',    'XL',   'X',    'IX',   'V',    'IV',   'I']
        i = 0
        res = 0
        sIdx = 0
        while sIdx < len(s):
            if s[sIdx:min(sIdx+len(unit[i]),len(s))] == unit[i]:
                res += table[i]
                sIdx += len(unit[i])
                # print(res)
            else:
                i += 1
            # print(i)
        return res
        
# @lc code=end

