import sys

list1 = str(sys.stdin.readline().strip())

s = set()
for i in range (len(list1)):
    a = list1[i:]+list1[:i]
    print(a)
    s.add(a)

print(len(s))