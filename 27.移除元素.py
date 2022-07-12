#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p]= nums[i]
                p += 1
        return p

# @lc code=end

