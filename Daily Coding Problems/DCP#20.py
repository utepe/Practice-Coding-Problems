'''
Given two singly linked lists that intersect at some point
find the intersecting node. The lists are non-cyclical.
'''
#assuming list is a linkedList 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#if referfencing worked properly this would be it
def getIntersectionNode(headA: ListNode, headB: ListNode):
    pA = headA
    pB = headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    return pA

#valid version of doing it with regular lists
def intersecionNode(list1, list2):
    pList1 = list1
    pList2 = list2
    while pList1 != pList2:
        pList1 = pList1[1:] if len(pList1) > 0 else list2
        pList2 = pList2[1:] if len(pList2) > 0 else list1
    return pList1

def setLinkedList(list):
    next = None
    for i in list[::-1]:
        node = ListNode(i)
        node.next = next
        next = node
    return next

def printList(head):
    current = head
    next = None
    while current != None:
        print(current.val)
        current = current.next
                
# headA = setLinkedList([4,1,8,4,5])
# headB = setLinkedList([5,0,1,8,4,5])
# print(getIntersectionNode(headA, headB))
print(intersecionNode([4,1,8,4,5], [5,0,1,8,4,5]))
print(intersecionNode([3, 7, 8, 10], [99, 1, 8, 10]))