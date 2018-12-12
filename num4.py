class resolution:
    """
    题目

    用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
    思路
    当stack2中不为空时，在stack2中的栈顶元素是最先进入队列的元素，可以弹出。
    如果stack2为空时，我们把stack1中的元素逐个弹出并压入stack2。
    由于先进入队列的元素被压倒stack1的栈底，经过弹出和压入之后就处于stack2的栈顶，
    有可以直接弹出。如果有新元素d插入，我们直接把它压入stack1即可。
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,node):
        self.stack1.append(node)
    def pop(self,node):
        if len(self.stack2) == 0:
            self.stack1.append(self.stack1.pop())
        return self.stack2.pop()