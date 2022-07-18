#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start
class Solution(object):
    def partialBubbleSort(self, nums, start, end):
        while end > start:
            for i in range(start, end):
                if nums[i+1]<nums[i]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
            end -= 1
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i >= 1:
            if nums[i-1] >= nums[i]:
                i -= 1
            else:
                self.partialBubbleSort(nums,i,len(nums)-1)
                for j in range(i, len(nums)):
                    if nums[i-1] < nums[j]:
                        nums[i-1],nums[j] = nums[j],nums[i-1]
                        break
                return nums
        nums.sort()
        return nums
            

        # 121 832->121 238 -> 122 138
        # 125 832->125 238 -> 128 235
        # 125 862->125 268->126 258
        # 125 8->128 5
        # 12 54->12 45->14 25
# @lc code=end

# ans = Solution().nextPermutation([1,2,3])
# print(ans)