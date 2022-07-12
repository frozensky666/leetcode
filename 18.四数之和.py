#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        i = 0
        j = 0
        while i < len(nums)-2: # python的for循环没办法给迭代变量赋值（差评）
            j = i + 1
            while j < len(nums)-1:
                l = j+1
                r = len(nums)-1
                while l < r:
                    tmpSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmpSum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l + 1 < r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
                        r -= 1
                    elif tmpSum < target:
                        l += 1
                    else:
                        r -= 1
                while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                    j += 1
                j += 1
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return res

# s = Solution()
# s.fourSum([2,2,2,2,2],8)

# @lc code=end

