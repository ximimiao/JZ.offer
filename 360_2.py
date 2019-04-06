n1 = (input().strip('\n').split(' '))
N = int(n1[0])
if N<1:
    print(-1)
if M>pow(10,5):
    print(-1)
M = int(n1[1])
n2 = (input().strip('\n').split(' '))
A = []
for i in range(len(n2)):
    A.append(int(n2[i]))
if len(A)!=N:
    print(-1)
l = []
for i in range(M):
    m = []
    n3 = (input().strip('\n').split(' '))
    for i in range(len(n1)):
        m.append(int(n3[i]))
    l.append(m)

def sort_arr(a,b):
    if b[1]>=len(a):
        return -1
    if b[0]==0:
        temp = a[:b[1]]
        temp.sort()
        for data in a[b[1]:]:
            temp.append(data)
        return temp
    if b[0]==1:
        temp = a[:b[1]]
        temp.sort(reverse = True)
        for data in a[b[1]:]:
            temp.append(data)
        return temp
    else:
        return -1
for i in range (len(l)):
    A = sort_arr(A,l[i][:])
re = ''
for s in A:
    re+=str(s)
    re+=' '
print(re)