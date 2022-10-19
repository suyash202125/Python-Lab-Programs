from dataclasses import dataclass


@dataclass
class knapsack_item:
    w : int = 0
    p : int = 0

    def __init__(self, w, p):
        self.w = w
        self.p = p


@dataclass
class knapsack:
    def __init__(self):
        self.d = []

    def add(self, item):
        self.d.append(item)

    def display(self):
        print("knapsack:",self.d)


t1 = knapsack_item(5, 20)
t2 = knapsack_item(4, 17)

i1 = knapsack.add(t1)
i2 = knapsack.add(t2)

i1.display()