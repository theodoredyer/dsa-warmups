class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.maxCnt = 0
        self.stack = {}

    def push(self, val: int) -> None:
        valcnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valcnt

        if valcnt > self.maxCnt:
            self.maxCnt = valcnt
            self.stack[valcnt] = []

        self.stack[valcnt].append(val)


    def pop(self) -> int:

        resval = self.stack[self.maxCnt].pop()
        self.cnt[resval] -= 1

        if not self.stack[self.maxCnt]:
            self.maxCnt -= 1

        return resval
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()