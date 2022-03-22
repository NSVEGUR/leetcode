from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        (l1, l2) = self._largest(l1, l2)
        head = None
        carry = 0
        while l2 is not None:
            val = l1.val + l2.val + carry
            if val >= 10:
                val -= 10
                carry = 1
                head = self._addToList(head, val)
            else:
                carry = 0
                head = self._addToList(head, val)
            l2 = l2.next
            l1 = l1.next
        while l1 is not None:
            val = l1.val + carry
            if val >= 10:
                val -= 10
                carry = 1
                head = self._addToList(head, val)
            else:
                carry = 0
                head = self._addToList(head, val)
            l1 = l1.next
        if carry is 1:
            head = self._addToList(head, 1)
        return head

    def _largest(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        len1 = 0
        len2 = 0
        temp1 = l1
        temp2 = l2
        while temp1 != None:
            len1 += 1
            temp1 = temp1.next
        while temp2 != None:
            len2 += 1
            temp2 = temp2.next
        if len2 >= len1:
            return (l2, l1)
        return (l1, l2)

    def _addToList(self, head: Optional[ListNode], val: int):
        temp = head
        if temp == None:
            head = ListNode(val)
            return head
        while temp.next != None:
            temp = temp.next
        temp.next = ListNode(val)
        return head


# Linked list printing (JUST FOR DEV)
    # def _printList(self, head: Optional[ListNode]):
    #     temp = head
    #     while temp != None:
    #         print(temp.val)
    #         temp = temp.next

# sol = Solution()

# # hard coded list
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(9)
# l1.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next.next = ListNode(9)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
# l2.next.next.next = ListNode(9)

# sol.addTwoNumbers(l1, l2)
