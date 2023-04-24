class Calculator:
    num = 10

    def getData(self):
        print("I am in get data")

    #constructor
    def __init__(self, a , b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am in parent class constructor ")

    def SumOfTwoNumbers(self):
        return self.firstNumber + self.secondNumber+Calculator.num+self.num


obj = Calculator(2,3)
obj.getData()
print("{} {}".format("Class variable", obj.num))
print("{} {}".format("Instance variable", obj.SumOfTwoNumbers()))

obj1 = Calculator(9,10)
obj1.getData()
print("{} {}".format("Class variable", obj1.num))
print("{} {}".format("Instance variable", obj1.SumOfTwoNumbers()))
