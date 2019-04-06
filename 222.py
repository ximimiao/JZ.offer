import sys
n = []
for line in sys.stdin:
    l = []
    a = line.split()
    for i in a :
        l.append(int(i))
    n.append(l)
a = n[0][0]
k = n[0][1]
q = n[1]
q.sort()
count = 0
def dao(n,k):
    for i in range(len(n)-1,0,-1):
        summ = 0
        summ+= ( n[i] - n[i-1])
        if summ>k:
            print(n)
        else:
            n[i] = n[i-1]
    return n
while(sum(q)>q[0]*a):
    q = dao(q,k)
    count +=1
print(count)











