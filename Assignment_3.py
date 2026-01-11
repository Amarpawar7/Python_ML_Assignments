# 1.

# A user-defined function is a function created by the programmer using the 'def' keyword to perform a specific repeating instruction/block of code in a program

def multiply(a,b):
    return (a*b)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2.

# Functions with parameters accepts value from the user
def add(a,b):
    return (a+b)
#Functions without parameters doesn't accept any values 
def start():
    print("Jay Ganesh")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. 

def fun():
    x = 10
    print(x)

fun()                       #at this point the code will execute this function and gives us the output as 10
#print(x)                    # here we will get an error coz x is a local variable and not global variable 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4.

def start():
    print("Jay Ganesh")

# Default returnof such function is 'None'

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5.

# print() returns nothing ,it is just used to display content/output 
# return is used to send a particular value to display,it ends the exeution of a function

def start():
    print("Jay Ganesh")

def end():
    return "Jay Ganesh"


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6.

import sys

x=input("Enter a value: ")
print("Data type of x is : ",type(x))
print("Memory address of x is :",id(x))
print("Size in bytes is :",sys.getsizeof(x))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7.

a = 11
print(type(a))         # int
a = 11.21
print(type(a))         # float
a ="Jay"
print(type(a))         # str

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#8.

x=100     #Python is dynamically typed,so variables don't need to be declared explicitly
# in C/Java variable type must be declared

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 9.

#Yes, coz python supports dynamic typing,which allows a variable to refer to values of different datatypes at different times.
 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#10.

#Python uses automatic memory management
#Python automatically allocates memory when objects are created and frees memory when objects are no longer referenced.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

