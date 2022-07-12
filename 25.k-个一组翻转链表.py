#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0, head)
        p = dummyHead
        short = False
        while p.next:
            pNext, short = self.reverseK(p, k)
            if short:
                pNext, short = self.reverseK(p, k)
            p = pNext

        return dummyHead.next

    def reverseK(self, dummyHead, k):
        #    p  q         
        # d->1->2->3->4
        p = dummyHead.next
        if p.next == None:
            return (p, False)
        q = p.next
        while q and k > 1:
            p.next = q.next
            q.next = dummyHead.next
            dummyHead.next = q
            q = p.next
            k -= 1
        return (p, k>1)
        
        
        
# @lc code=end

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# s = Solution()
# s.reverseKGroup(n,2)