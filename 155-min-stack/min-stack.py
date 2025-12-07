class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_num.append(val)
        else:
            self.stack.append(val)
            self.min_num.append(min(self.min_num[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_num.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()