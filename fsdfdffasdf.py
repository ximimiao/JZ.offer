num = int(input().strip('\n'))
l = []
for i in range(num):
    m = []
    n1 = (input().strip('\n').split(' '))
    for i in range(len(n1)):
        m.append(int(n1[i]))
    l.append(m)

for i in range (len(l)):
    summ=0
    for j in range(len(l[i])):
        summ+=l[i][j]*(j+1)
    print(summ//4)
