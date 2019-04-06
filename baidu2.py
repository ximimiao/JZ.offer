import sys

list1 = str(sys.stdin.readline().strip())
list2 = str(sys.stdin.readline().strip())
num = int(sys.stdin.readline().strip())
l = []
for i in range(num):
    m = []
    n1 = (sys.stdin.readline().strip().split(' '))
    for i in range(len(n1)):
        m.append(int(n1[i]))
    l.append(m)
def func(a,b,l,r):
    target_s = a[l:r+1]
    count = 0
    while target_s.find(b) is not -1:
        target_s = target_s[target_s.find(b)+1:]
        count += 1
    return count
for i in range (len(l)):
    print(func(list1,list2,l[i][0],l[i][1]))