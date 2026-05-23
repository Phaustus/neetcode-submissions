# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        h = ListNode()
        curr = h
        l = []

        while head:
            l.append(head.val)
            head = head.next

        for i in range(len(l) - 1, -1, -1):
            curr.val = l[i]
            if i > 0:
                curr.next = ListNode()
                curr = curr.next

        return h

            