# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        temp = None
        car = 0
        while l1 is not None or l2 is not None:
            value = car
            if l1 is not None:
                value += l1.val  
                l1 = l1.next
            if l2 is not None:
                value += l2.val 
                l2 = l2.next
            node = ListNode(value%10)
            car = int(value/10)
            if temp is None:
                head = node 
                temp = node
            else:
                temp.next = node
                temp = temp.next

        if car > 0: temp.next = ListNode(car)
        return head