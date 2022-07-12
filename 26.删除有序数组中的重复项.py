#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        p = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[p]:
                p += 1
                nums[p] = nums[i]
        return p+1

# @lc code=end

# s = Solution()
# s.removeDuplicates([1,1,2])

