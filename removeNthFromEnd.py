from typing import List
from unittest import TestCase, main


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        blank_node = ListNode(-1)
        blank_node.next = head

        tail_node = blank_node
        head_node = blank_node

        while n > 0:
            tail_node = tail_node.next
            n -= 1

        while tail_node.next != None:
            tail_node = tail_node.next
            head_node = head_node.next

        head_node.next = head_node.next.next

        return blank_node.next


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.sol = Solution()



    def test_first_case(self):
        ans = self.sol.removeNthFromEnd(head=[1, 2, 3, 4, 5], n=2)
        self.assertEqual(ans, [1, 2, 3, 5])
