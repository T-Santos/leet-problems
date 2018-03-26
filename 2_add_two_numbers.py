'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    def create_linked_list(number):

        head = None
        current = None
        for number in list(str(number))[::-1]:

            if not head:
                head = ListNode(number)
                current = head
            else:
                new_node = ListNode(number)
                current.next = new_node
                current = new_node
        return head

    def list_to_number(head):

        current = head
        num_list = []

        while current:
            num_list.append(current.val)
            current = current.next

        return sum([int(num)*(10**off) for off,num in enumerate(num_list)])
    
    int1 = list_to_number(l1)
    int2 = list_to_number(l2)
    int3 = int1+int2
    
    return create_linked_list(int3)