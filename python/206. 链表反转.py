# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     # 递归写法
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head == None: return None
#         head, tail = self.sub_reverseList(head)
#         return head
#
#     def sub_reverseList(self,head):
#         if head.next == None:
#             return head, head
#         nhead, tail = self.sub_reverseList(head.next)
#         tail.next = head
#         head.next = None
#         return nhead, head

class Solution(object):
    # 非递归写法
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        dummy = ListNode(0)
        dummy.next = head
        pre, p = head, head.next
        while p:
            pre.next = p.next
            p.next = dummy.next
            dummy.next = p
            p = pre.next

        return dummy.next
