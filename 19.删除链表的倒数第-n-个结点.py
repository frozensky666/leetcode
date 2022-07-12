#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0, head)
        q = head
        while n > 0:
            q = q.next
            n -= 1
        prev = dummyHead
        while q:
            prev = prev.next
            q = q.next
        prev.next = prev.next.next
        return dummyHead.next

        
# @lc code=end

