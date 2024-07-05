class EvenNumbers:
    def __init__(self,start=0,end=1):
        if start > end:
            start,end = end,start
        self.start = start
        self.end = end
    def __iter__(self):
        self.i = self.start
        return self
    def __next__(self):
        self.i +=1
        if self.i-1>self.end:
            raise StopIteration()
        if self.i%2 == 1:
            return self.i-1
        if self.i%2 == 0:
            self.i +=2
            return self.i-2

en = EvenNumbers(10,25)
for i in en:
    print(i)
