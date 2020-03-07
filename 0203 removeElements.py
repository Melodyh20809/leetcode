# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val) :
        
        L=l=ListNode(0)
        while head:
            if head.val!=val:
                l.next=ListNode(head.val)
                l=l.next
            head=head.next
        return L.next

x=Solution()
A=a=ListNode(0)
a.next=ListNode(1)
a=a.next
a.next=ListNode(2)
print(A)
result=x.removeElements(A,1)
print(result)


        