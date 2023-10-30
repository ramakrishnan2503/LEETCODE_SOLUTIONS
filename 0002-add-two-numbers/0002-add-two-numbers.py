# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def make_ll(self,number):
            head = ListNode()
            current = head
            while number>0:
                digit = number %10
                current.next = ListNode(digit)
                current = current.next
                number = number//10
            if head.next:
                return head.next
            else:
                return head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x=''
        y=''
        while l1!=None:
            x+=str(l1.val)
            l1=l1.next
        while l2!=None:
            y+=str(l2.val)
            l2=l2.next
        x=int(x[::-1])
        y=int(y[::-1])
        return self.make_ll(x+y)