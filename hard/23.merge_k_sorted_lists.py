# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        val = []
        for i in lists:
            temp = i
            while temp is not None:
                val.append(temp.val)
                temp = temp.next
        temp = None
        head = None
        for i in sorted(val):
            node = ListNode(i)
            if temp is None:
                head = node # assigning values
                temp = node 
            else:
                temp.next = node # assigning next values to head, # as node will change on each iteration
                temp = temp.next
        return head            