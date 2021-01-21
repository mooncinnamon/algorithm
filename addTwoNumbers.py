# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        result = head
        tail_sum = 0
        while l2 or l1 or tail_sum:
            sum = 0
            if not l1 and l2:
                sum = l2.val
            elif not l2 and l1:
                sum = l1.val
            elif l1 and l2:
                sum = l1.val + l2.val
            head_sum = sum % 10 + tail_sum if (sum % 10 + tail_sum) < 10 else (sum % 10 + tail_sum) % 10
            tail_sum = sum // 10 if (sum % 10 + tail_sum) < 10 else sum // 10 + (sum % 10 + tail_sum) // 10

            result.val = head_sum
            result.next = ListNode()

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if l1 is None and l2 is None and tail_sum is 0:
                result.next = None
            else:
                result = result.next

        return head


def make_node(array):
    head = ListNode()
    result = head
    for data in range(len(array)):
        result.val = array[data]
        if data is not len(array) - 1:
            result.next = ListNode()
            result = result.next

    return head


if __name__ == '__main__':
    l1s = make_node([9, 9, 9, 9, 9, 9, 9])

    l2s = make_node([9, 9, 9, 9])

    Solution().addTwoNumbers(l1=l1s, l2=l2s)
