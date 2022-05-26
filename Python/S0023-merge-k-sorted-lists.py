"""
Given an array of linked-lists lists, each linked list is sorted in ascending order.

Merge all the linked-lists into one sort linked-list and return it.

 
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

 
Constraints:
	k == lists.length
	0 <= k <= 10^4
	0 <= lists[i].length <= 500
	-10^4 <= lists[i][j] <= 10^4
	lists[i] is sorted in ascending order.
	The sum of lists[i].length won't exceed 10^4.


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
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

        lists = list(filter(lambda l: l != None,lists))
        
        while len(lists) >= 2:
            tnode = ListNode()
            choose(tnode,lists[0],lists[1])
            lists.remove(lists[0])
            lists.remove(lists[0])
            lists.append(tnode.next)
        if not any(lists):
            return None
        return lists.pop()


if __name__ == '__main__':

    def tolist(listOfnums):
        def array2list(nums):
            dummyhead = ListNode(0,None)

            ptr=dummyhead
            for n in nums:
                ptr.next = ListNode(n,None)
                ptr = ptr.next
            return dummyhead.next

        return [array2list(nums) for nums in listOfnums]

    def lst2array(head):
        lst=[]
        n = head
        while n:
            lst.append(n.val)
            n = n.next
        return lst

    assert lst2array(Solution().mergeKLists(tolist([[1,4,5],[1,3,4],[2,6],[]]))) == [1,1,2,3,4,4,5,6]
    assert lst2array(Solution().mergeKLists(tolist( []))) == []
    assert lst2array(Solution().mergeKLists(tolist([[]]))) == []
