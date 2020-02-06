class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        L=l=ListNode(0)
        a=head.val-1
        while head:
            if a==head.val:
                head=head.next
            else:
                a=head.val
                L.next=ListNode(head.val)
                L=L.next
                head=head.next
        return l.next


x=Solution()
l1 = l = ListNode(1)
l.next = ListNode(1)
l = l.next
l.next = ListNode(5)

result=x.deleteDuplicates(l1)
while result:
    print(result.val)
    result = result.next
print(result)