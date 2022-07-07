#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                tmpSum = nums[i] + nums[l] + nums[r]
                if tmpSum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l + 1 < r and nums[l+1] == nums[l]: 
                        l += 1
                    l += 1
                    r -= 1
                elif tmpSum < 0:
                    l += 1
                else:
                    r -= 1
        return res

# @lc code=end

# -4 -1 -1 0 1 1 2
