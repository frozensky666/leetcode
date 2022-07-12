#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n, 0, [], 0, 0, res)
        return res

    def dfs(self, n, start, path, leftBracket, rightBracket, res):
        if rightBracket > leftBracket:
            return
        if leftBracket > n:
            return
        if start == n*2:
            if rightBracket == leftBracket:
                res.append(''.join(path))
            return
            
        path.append('(')
        self.dfs(n, start+1, path, leftBracket+1, rightBracket,res)
        path.pop()

        path.append(')')
        self.dfs(n, start+1, path, leftBracket, rightBracket+1,res)
        path.pop()
# @lc code=end


# s = Solution()
# s.generateParenthesis(3)