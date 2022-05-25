"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def count(head):
            if head:
                return 1 + count(head.next)
            else:
                return 0

        cnt = count(head)
        if cnt == n:
            return head.next
            
        tmpnode = head
        for i in range(cnt - n - 1):
            tmpnode = tmpnode.next
        
        if tmpnode.next:
            tmpnode.next = tmpnode.next.next
            return head
        else:
            return None


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

    assert lst2array(Solution().removeNthFromEnd(array2list([1,2]), 2)) == [2]
    assert lst2array(Solution().removeNthFromEnd(array2list([1,2]), 1)) == [1]
    assert lst2array(Solution().removeNthFromEnd(array2list([1]), 1)) == []
    assert lst2array(Solution().removeNthFromEnd(array2list([1,2,3,4,5]), 2)) == [1,2,3,5]

