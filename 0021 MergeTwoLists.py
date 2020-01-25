#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        L=l=ListNode(0)
        while l1 and l2:
            if l1.val>=l2.val:
                L.next=ListNode(l2.val)
                L=L.next
                l2=l2.next
            else:
                L.next=ListNode(l1.val)
                L=L.next
                l1=l1.next
        L.next=l1 or l2   
        return l.next


x=Solution()
l1 = l = ListNode(1)
l.next = ListNode(2)
l = l.next
l.next = ListNode(5)

l2 = l = ListNode(1)
l.next = ListNode(3)
l = l.next
l.next = ListNode(4)

result=x.mergeTwoLists(l1, l2)
while result:
    print(result.val)
    result = result.next
print(result)