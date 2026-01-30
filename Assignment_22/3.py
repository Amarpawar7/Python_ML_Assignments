class Arithmetic:
    def __init__(self):
        self.Value1 =0
        self.Value2 =0

    def Accept(self):
        self.Value1 =int(input("Enter Value1: "))
        self.Value2 =int(input("Enter Value2: "))

    def Addition(self):
        return(self.Value1 + self.Value2)

    def Subtraction(self):
        return(self.Value1 - self.Value2)

    def Multiplication(self):
        return(self.Value1 * self.Value2)

    def Division(self):
        if(self.Value2 != 0):
            return(self.Value1 / self.Value2)
        else:
            print("Division by zero is not allowed")


obj1 = Arithmetic()
obj2 = Arithmetic()

obj1.Accept()
print("Addition is : ",obj1.Addition())
print("Subtraction is : ",obj1.Subtraction())
print("Multiplication is : ",obj1.Multiplication())
print("Division is : ",obj1.Division())
print("-"*40)

obj2.Accept()
print("Addition : ",obj2.Addition())
print("Subtraction : ",obj2.Subtraction())
print("Multiplication is : ",obj2.Multiplication())
print("Division is : ",obj2.Division())