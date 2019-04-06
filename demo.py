def money():
    num1 = list(map(str, input().split(' ')))
    length = len(num1)
    que = []
    for i in range (length):
        temp = num1[i].split(',')
        temp_int = [int(x) for x in temp]
        que.append(temp_int)
    que.sort(key=lambda x:x[0])
    merge = []
    for que_ in que:
        if not merge or que_[0]>merge[-1][-1]:
            merge.append(que_)
        else:
            merge[-1][-1] = max(merge[-1][-1],que_[-1])
    print(merge)
    s = ''
    for i in merge:
        s += ','.join(str(x) for x in i)
        s += ' '


    print(s)





money()