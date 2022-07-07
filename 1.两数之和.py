#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmpDict = {}
        for i in range(0, len(nums)):
            num = nums[i]
            idx = tmpDict.get(target - num)
            if idx != None:
                return [idx,i]
            else:
                tmpDict[num] = i
        # print(tmpDict)


# @lc code=end

