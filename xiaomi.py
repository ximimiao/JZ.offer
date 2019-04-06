import sys

list1 = (sys.stdin.readline().strip().split())
list2 = (sys.stdin.readline().strip().split())

l1 = []
l2 = []

for node in list1:
    l1.append(int(node))

for node in list2:
    l1.append(int(node))

print(l1)

l1.sort()

s = ''

for i in l1:
    s+=str(i)
    s+=' '
print(s)