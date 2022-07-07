#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        minBias = 100000
        nums.sort()
        for i in range(0, len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                tmpSum = nums[i] + nums[l] + nums[r]
                bias = abs(tmpSum-target)
                # print(tmpSum)
                # print(bias)
                if bias < minBias:
                    minBias = bias
                    res = tmpSum
                if tmpSum < target:
                    l += 1
                elif tmpSum > target:
                    r -= 1
                else:
                    return target
        return res
# @lc code=end

