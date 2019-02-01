def bubblesort(numList):
    #冒泡排序
    # 优化前，时间复杂度o(n2)
    for i in range (len(numList) -1):
        for j in range(i,len(numList)-1):
            if numList[j] > numList [j+1]:
                numList[j],numList[j+1] = numList[j+1],numList[j]
        print(numList)
def optibubbulesort(numList):
    """
    优化后
    :param numList:
    :return:
    """
    for i in range (len(numList) -1):
        bbalance = False
        for j in range(i,len(numList)-1):
            if numList[j] > numList [j+1]:
                numList[j],numList[j+1] = numList[j+1],numList[j]
                bbalance = True
        print(numList)
        if bbalance is not True:
            break
    return numList


if __name__ == '__main__':
    listnum = [1,2,5,7,3,9,4]
    optibubbulesort(listnum)