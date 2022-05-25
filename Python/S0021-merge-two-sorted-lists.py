"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyhead = ListNode()

        def choose(head,l1,l2):
            if l1 == None or l2 == None:
                head.next = l1 if l1 else l2
                return
            
            if l1.val <= l2.val:
                head.next = ListNode(l1.val)
                choose(head.next,l1.next,l2)
            else:
                head.next = ListNode(l2.val)
                choose(head.next,l1,l2.next)

        choose(dummyhead,l1,l2)
        return dummyhead.next


if __name__ == '__main__':
    def array2list(nums):
        dummyhead = ListNode(0,None)

        ptr=dummyhead
        for n in nums:
            ptr.next = ListNode(n,None)
            ptr = ptr.next
        return dummyhead.next

    def lst2array(head):
        lst=[]
        n = head
        while n:
            lst.append(n.val)
            n = n.next
        return lst

    assert lst2array(Solution().mergeTwoLists(array2list([1,2,4]), array2list([1,3,4]))) == [1,1,2,3,4,4]

