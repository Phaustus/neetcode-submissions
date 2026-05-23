class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = set()

        while head != None:
            if head in l:
                return True
            l.add(head)
            head = head.next
        return False