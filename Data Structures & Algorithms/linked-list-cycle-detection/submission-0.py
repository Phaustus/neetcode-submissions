
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # lista koja sadrzi kopije svih node-ova pa ih uporedi svaki put kada naidje na novi
        l = set()

        while head != None:
            len_pre = len(l)
            l.add(head) 
            len_post = len(l)

            if len_pre == len_post:
                return True
            head = head.next
        return False