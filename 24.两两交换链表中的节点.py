#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0, head)
        p = dummyHead
        while(p.next):
            nodeOne = p.next
            nodeTwo = None
            if nodeOne.next:
                nodeTwo = nodeOne.next
            if nodeTwo:
                p.next = nodeTwo
                nodeOne.next = nodeTwo.next
                nodeTwo.next = nodeOne
            p = nodeOne
        return dummyHead.next


# @lc code=end

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
# s = Solution()
# s.swapPairs(n)