#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start


class Solution(object):

    tables = [
        None,
        None,
        ['a','b','c'],
        ['d','e','f'],
        ['g','h','i'],
        ['j','k','l'],
        ['m','n','o'],
        ['p','q','r','s'],
        ['t','u','v'],
        ['w','x','y','z']
    ]

    def dfs(self, digits, start, path, res):
        if len(path) == len(digits):
            res.append("".join(path))
            return
        for i in range(start, len(digits)):
            chars = self.tables[int(digits[i])]
            for c in chars:
                path.append(c)
                self.dfs(digits, i+1, path, res)
                path.pop()

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "" or digits == None:
            return []
        res = []
        self.dfs(digits=digits, start=0, path=[], res=res)
        return res
# @lc code=end

