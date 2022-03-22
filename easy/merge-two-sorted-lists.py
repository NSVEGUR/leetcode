from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None or list2 == None:
            if list1 == None:
                return list2
            else:
                return list1
        (list1, list2) = self._findSmallest(list1, list2)
        head = None
        temp1 = list1
        temp2 = list2
        while temp1 != None and temp2 != None and temp1.next != None:
            head = self._addToList(head, temp1.val)
            while temp2 != None and temp2.val <= temp1.next.val:
                head = self._addToList(head, temp2.val)
                temp2 = temp2.next
            temp1 = temp1.next
        while temp2 != None and temp2.val <= temp1.val:
            head = self._addToList(head, temp2.val)
            temp2 = temp2.next
        while temp1 != None:
            head = self._addToList(head, temp1.val)
            temp1 = temp1.next
        while temp2 != None:
            head = self._addToList(head, temp2.val)
            temp2 = temp2.next
        return head

    def _findSmallest(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        tuple = None
        if list1.val > list2.val:
            tuple = (list2, list1)
        else:
            tuple = (list1, list2)
        return tuple

    def _addToList(self, head: Optional[ListNode], val: int):
        temp = head
        if temp == None:
            head = ListNode(val)
            return head
        while temp.next != None:
            temp = temp.next
        temp.next = ListNode(val)
        return head
