# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 0
        arrayList = []
        while True:
            if eval('l1'+ i * '.next') == None:
                break
            arrayList.append(eval('l1'+ i * '.next').val)
            i += 1
        i = 0
        while True:
            if eval('l2' + i * '.next') == None:
                break
            arrayList.append(eval('l2'+ i * '.next').val)
            i += 1
        if len(arrayList) == 0:
            return l1
        arrayList.sort()
        arrayResult = []
        for i in range(len(arrayList)):
            if i == 0:
                a = ListNode(arrayList[-1], None)
            else:
                a = ListNode(arrayList[-i-1], arrayResult[i-1])
            arrayResult.append(a)
        return arrayResult[-1]