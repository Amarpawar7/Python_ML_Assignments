# 1.Write a program to Display : Value,Type,Memory Address for a variable using appropriate build-in functions

x=21
print("Value of the variable x is : ",x)
print("Type of variable x is : ",type(x))
print("Memory Address of variable x is : ",id(x))


# 2.

a=10
b=10
print(id(a)==id(b))   #this will give output as "True",coz this represents that there are two variables which r immutable integer objects So both refers to the same value as well as address

a=[10]
b=[10]
print(id(a)==id(b))   #this will give output as "False" Here, these two variables refer Two different elements of list that may have same content Coz list is mutable but are stored at two different addresses.


# 3.

# id() returns the memory address of a particular object
# id() can be same for variable,but cannot be same for 2 different elements of a list


# 4.

#getsizeof() gives us the memory size of an object in bytes
#Because it depends on how much amount of data/information is stored by different datatypes


#5

a=10
b=10
print(id(a)== id(b))            #output will be true


# 6.

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

print("Addition of given number is : ",a+b)
print("Subtraction of given number is : ",a-b)
print("Multiplication of given number is : ",a*b)
print("Division of given number is : ",a/b)


# 7.

# Because python reads every input as string by default


# 8. 

x=input("Enter number : ")
print(type(x))                  #Output wil be 'str', because input() function always returns a string by default if user didn't mention its datatype


# 9.

name = input("Enter name: ")
age = int(input("Enter age: "))

print("Hello ",name," you will turn ",(age+1) , "next year.")


# 10.

print("10" + "20")        # here the values 10 and 20 are treated as string so tey will add up sequencially i.e. 1020 will be the output 
print(10 + 20)            # here these values of 10 and 20 are treated as integer values so they will add up mathematically i.e. 30 will be the output
