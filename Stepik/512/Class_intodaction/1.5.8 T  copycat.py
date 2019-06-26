class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0

    def can_add(self, v):
        return self.current + v <= self.capacity

    def add(self, v):
        self.current += v


x = MoneyBox(10)
a = 5
if x.can_add(a):
    print(x.add(a))
print(a)


