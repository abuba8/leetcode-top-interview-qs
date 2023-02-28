# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = []
        while list1 is not None or list2 is not None:
            if list1 is not None:
                temp.append(list1.val)
                list1 = list1.next
            else:
                temp.append(list2.val)
                list2 = list2.next

        pointer = None
        head = None
        for x in sorted(temp):
            node = ListNode(x)
            if pointer is None:
                head = node 
                pointer = node
            else:
                pointer.next = node
                pointer = pointer.next

        return head