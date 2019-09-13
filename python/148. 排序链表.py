# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        nhead = slow.next

        slow.next = None

        head = self.sortList(head)
        nhead = self.sortList(nhead)

        return self.merge(head, nhead)

    def merge(self, h1, h2):
        dummy = ListNode(0)
        r = dummy
        p, q = h1, h2
        while p and q:
            if p.val < q.val:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next
            r = r.next

        if p: r.next = p

        if q: r.next = q

        return dummy.next
