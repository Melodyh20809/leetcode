class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L=[]

    def push(self, x: int) -> None:
        if not L:
            self.L.append(x,x)
        else:
            self.L.append(x,min(x,L[-1][-1]))
    
    def pop(self) -> None:
        self.L.pop()

    def top(self) -> int:
        return self.L[-1][0]

    def getMin(self) -> int:
        return self.L[-1][-1]
