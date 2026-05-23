
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # lista koja sadrzi kopije svih node-ova pa ih uporedi svaki put kada naidje na novi
        l = set()

        while head != None:
            if head in l:
                return True
            else:
                l.add(head)
            head = head.next
        return False