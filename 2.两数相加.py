#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         num1 = 0
#         base = 1
#         while l1 != None:
#             num1 = num1 + l1.val * base
#             l1 = l1.next
#             base *= 10
#         num2 = 0
#         base = 1
#         while l2 != None:
#             num2 = num2 + l2.val * base
#             l2 = l2.next
#             base *= 10
#         resNum = num1 + num2
#         head = ListNode(resNum%10)
#         resNum = resNum // 10
#         p = head
#         while resNum != 0:
#             p.next = ListNode(resNum%10)
#             p = p.next
#             resNum = resNum // 10
#         return head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        p = head
        carry = 0
        while l1 or l2 or carry != 0:
            curNum = carry
            if l1:
                curNum += l1.val
                l1 = l1.next
            if l2:
                curNum += l2.val
                l2 = l2.next
            carry = curNum // 10
            curNum = curNum % 10
            p.next = ListNode(curNum)
            p = p.next
        return head.next



# @lc code=end

