from OopsDemo import Calculator


class ChildClassCalculator(Calculator):
    num2 = 10


    def __init__(self):
        Calculator.__init__(self, 5, 5)

    def ChildClassSummation(self):
        print("I am in child class class function")
        return self.num2 + self.num


obj2 = ChildClassCalculator()
print(obj2.ChildClassSummation())
