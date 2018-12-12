class resolution:
    """
    题目
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
    例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：
    给出的所有元素都大于0，若数组大小为0，请返回0。
   思路

我们注意到旋转之后的数组实际上可以划分为两个排序的字数组，
而且前面的字数组的元素大于或者等于后面字数组的元素。
我们还注意到最小的元素刚好是这两个字数组的分界线。
在排序的数组中可以用二分查找实现O(logn)的查找。
本题给出的数组在一定程度上是排序的，因此我们可以试着用二分查找法的思路来寻找这个最小的元素。
    """
    def minnumInrotate(self,rotateArray):
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray)-1
        mid = 0
        while rotateArray[left] > rotateArray[right]:
            if right - left == 1:
                mid = right
                break
            mid = left + (right - left)//2
            if rotateArray[mid] == rotateArray[right] and rotateArray[mid]== rotateArray[left]:
                return self.mininorder(rotateArray,left,right)
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return rotateArray[mid]


    def mininorder(self,array,left,right):
        result = array[left]
        for i in range(left+1,right+1):
            if array[i] < result:
                result = array[i]
        return result
