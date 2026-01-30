class Demo:
    Value =0

    def __init__(self,No1,No2):
        self.No1 =No1
        self.No2 =No2

    def fun(self):
        print("Inside fun : No1 = ",self.No1 ,"and No2 = ",self.No2)

    def gun(self):
        print("Inside gun : No1 = ",self.No1 ,"and No2 = ",self.No2)


obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()
