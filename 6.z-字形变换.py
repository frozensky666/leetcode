#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = ""
        for row in range(numRows):
            idx = row
            if idx >= len(s):
                break
            # print (s[idx], end="")
            res += s[idx]
            blanks = (numRows - 1 - row, row)
            i = 0
            while idx + blanks[i]*2 < len(s):
                if blanks[i] != 0:
                    # for _ in range(blanks[i]-1):
                        # print(" ", end="")
                    # print (s[idx + blanks[i]*2], end="")
                    res += s[idx + blanks[i]*2]
                idx = idx + blanks[i]*2
                i = (i + 1) % 2
            # print()
        return res

# s = Solution()
# print(s.convert("PAYPALISHIRING", 3))

# @lc code=end

# 0, 6, 12 (6[3],0[0]) - (numRows - 1) * 2
# 1, 5, 7, 11, 13 (4[2],2[1])
# 2, 4, 8, 10 (2[1],4[2])
# 3, 9 (0[0], 6[3])