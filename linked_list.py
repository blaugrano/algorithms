# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # neetcode
    # def swap(self, head):
    #     # for empty list input
    #     if not head:
    #         return None
    #
    #     new_head = head  # A) head -> null, end of the list
    #     if head.next:
    #         new_head = self.swap(head.next)  # A) keep pulling last head back
    #         head.next.next = head  # actual repointings
    #         head.next = None
    #     return new_head

    def swap(self, head):
        if head.next:
            new_head = self.swap(head.next)  # A) so retornando o ultimo node
            head.next.next = head            # B) rearrumando links na volta
            head.next = None                 # B) rearrumando links na volta
        else:
            new_head = head                  # A) so retornando o ultimo node
        return new_head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        return self.swap(head)

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

x = Solution().reverseList(a)

print(x.val)
while x.next:
    x = x.next
    print(x.val)