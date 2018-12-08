
class resolution:
    def printlist(self,listNode):
        """
        题目
        输入一个链表，返回一个反序的链表。

        使用列表的插入方法，每次插入数据，只插入在首位
        """
        result = []
        while(listNode):
            result.insert(0,listNode)
            listNode = listNode.next
        return result