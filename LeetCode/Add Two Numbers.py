# Add two numbers which are represented as two linkedlists in reverse order.
# link: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:             
        temp=ListNode(0)
        curr=temp
        root1,root2=l1,l2
        carry=0
        while root1 or root2:
            x,y=0,0
            if root1:
                x=root1.val
            if root2:
                y=root2.val
            sum=carry+x+y
            carry=sum//10
            curr.next=ListNode(sum%10)
            curr=curr.next
            if root1:root1=root1.next
            if root2:root2=root2.next
        if carry>0:
            curr.next=ListNode(carry)
        return temp.next
