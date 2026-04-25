class MinStack:

    def __init__(self):
       self.s = []
       self.mini_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.mini_s:
            if val <= self.mini_s[-1]:
                self.mini_s.append(val)
        else:
            self.mini_s.append(val)

    def pop(self) -> None:
        if self.s[-1] ==  self.mini_s[-1]:
            self.mini_s.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mini_s[-1]
