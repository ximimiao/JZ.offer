
import sys
class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None
class resolution:
    def Merge(self,x1,x2):
        phnew = ListNode(0)
        temp = phnew
        while(x1 != None and x2 != None):
            if x1.value <= x2.value:
                phnew.next = x1
                x1 = x1.next
            else:
                phnew.next = x2
                x2 = x2.next
            phnew = phnew.next
        if x1 is None:
            phnew.next = x2
        if x2 is None:
            phnew.next = x1
        return temp.next
list1 = ListNode(sys.stdin.readline().strip())
list2 = ListNode(sys.stdin.readline().strip())
print(list1.value,list2.value)
s = resolution()
a = s.Merge(list1,list2)
print(a.value)

