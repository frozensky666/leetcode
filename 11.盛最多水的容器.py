#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object): # 双指针
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        water = 0
        while l < r:
            water = max(water,min(height[l],height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water

# @lc code=end

