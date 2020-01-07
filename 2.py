# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        else :
            val = l1.val + l2.val
            result = ListNode(val%10)
            result.next = self.addTwoNumbers(l1.next,l2.next)
            if(val>9):
                result.next = self.addTwoNumbers(ListNode(1),result.next)
            return result