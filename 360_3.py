n1 = (input().strip('\n'))
n2 = (input().strip('\n').split(' '))
A = []
for i in range(len(n2)):
    A.append(int(n2[i]))
def func(A):
    if len(A) == 0:
        return -1
    mnius_list = list(range(-1,-1-len(A),-1))
    min_res = sum([abs(A[i]+mnius_list[i])for i in range(len(A))])
    for i in range(len(A)):
        res = sum([abs(A[i]+mnius_list[i])for i in range(len(A))])
        if res <min_res:
            min_res = res
        mnius_list.append(mnius_list.pop(0))
    return min_res
print(func(A))