import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = []
    summ = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        l = []
        for v in values:
            l.append(int(v))
        ans.append(l)
    num_1 = 0
    num_0 = 0
    for i in range(n):
        if ans[i][0]<0:
            num_0 += 1
        else:
            num_1 += 1
    if num_0 ==num_1:
        for i in range(n):
            summ += ans[i][1]
    if num_0>num_1:
        temp = []
        for i in range(n):
            if ans[i][0]>0:
                summ += ans[i][1]
            else:
                temp.append(ans[i][1])
        temp.sort(reverse=True)
        for i in range(num_1+1):
            summ += temp[i]
    if num_0<num_1:
        temp = []
        for i in range(n):
            if ans[i][0] < 0:
                summ += ans[i][1]
            else:
                temp.append(ans[i][1])
        temp.sort(reverse=True)
        for i in range(num_0+1):
            summ += temp[i]
    print(summ)