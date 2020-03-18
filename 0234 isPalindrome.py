# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        L=[0]
        while head:
            L.append(head.val)
            head=head.next
        for i in range(1,len(L)//2+1):
            if L[i]!=L[-i]:
                return False
        return True

x=Solution()
a=head=ListNode(1)
a.next=ListNode(2)
result=x.isPalindrome(head)
print(result)

