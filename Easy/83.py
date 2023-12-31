# 83. Remove Duplicates from Sorted List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        result = ""

        while self:
            result += str(self.val) + ','
            self = self.next
        
        return result

def deleteDuplicates(head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        while cur.val == cur.next.val:
            cur.next = cur.next.next
            if not cur.next:
                break
        cur = cur.next
    
    return head

head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print(head)
print(deleteDuplicates(head))
