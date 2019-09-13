# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        tail = dummy
        p, q = l1, l2

        while p and q:
            if p.val < q.val:
                tail.next = p
                p = p.next
            else:
                tail.next = q
                q = q.next
            tail = tail.next

        while p:
            tail.next = p
            tail = tail.next
            p = p.next

        while q:
            tail.next = q
            tail = tail.next
            q = q.next

        return dummy.next