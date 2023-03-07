# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        current_val = dummy_node
        #iterate through the two lists if both are not empty
        while list1 and list2:
            if list1.val < list2.val:
                current_val.next = list1 # tail.next points to list1 node
                list1 = list1.next
            else:
                current_val.next = list2
                list2 = list2.next
            current_val = current_val.next

        if list1:
            current_val.next = list1
        elif list2:
            current_val.next = list2

        return dummy_node.next
