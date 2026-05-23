class MinStack:

    def __init__(self):
        self.s = []
        self.m = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        if self.m == []:
            self.m.append(val)
            return
        if self.m[-1] >= val:
                self.m.append(val)
                
    def pop(self) -> None:
        if self.m[-1] == self.s[-1]:
            self.m.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return int(self.m[-1])