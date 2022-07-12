#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        q = []
        for eachList in lists:
            if eachList is not None:
                heapq.heappush(q, (eachList.val, eachList))
        dummyHead = ListNode()
        p = dummyHead
        while len(q)>0:
            p.next = heapq.heappop(q)[1]
            p = p.next
            if p.next:
                heapq.heappush(q,(p.next.val, p.next))
        return dummyHead.next
        
        
# @lc code=end

## method 1
# class Solution(object): # 归并
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         if len(lists) == 0:
#             return None

#         step = 1
#         while step < len(lists):
#             for i in range(0, len(lists), step*2):
#                 if i+step < len(lists):
#                     lists[i] = self.mergeTwoLists(lists[i], lists[i+step])
#             step *= 2
#         return lists[0]


#     def mergeTwoLists(self, list1, list2):
#         dummyHead = ListNode()
#         p = dummyHead
#         while list1 and list2:
#             if list1.val < list2.val:
#                 p.next = list1
#                 list1 = list1.next
#             else:
#                 p.next = list2
#                 list2 = list2.next
#             p = p.next
#         if list1:
#             p.next = list1
#         else:
#             p.next = list2
#         return dummyHead.next

## method 2
# from queue import PriorityQueue

# class Solution(object):
#     def mergeKLists(self, lists):
#         q = PriorityQueue()
#         for eachList in lists:
#             if eachList is not None:
#                 q.put((eachList.val, eachList))
#         dummyHead = ListNode()
#         p = dummyHead
#         while not q.empty():
#             p.next = q.get()[1]
#             p = p.next
#             if p.next:
#                 q.put((p.next.val, p.next))
#         return dummyHead.next