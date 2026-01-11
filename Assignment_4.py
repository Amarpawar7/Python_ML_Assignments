# 1.

# Lists are mutable,use more memory,slower,mostly used in cases where data modification is required
# Tuples are immutable,use less memory ,faster ,and is modtly used when data is fixed and there is no need to change

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2.

#Tuples are faster because they are immutable,so python doesn't need to handle modification overheads
#eg:storing id's of student 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.

lst = [10 , 20 , 30]
tpl = (10 , 20 , 30)

lst[0] = 100
tpl[0] = 100       #This line will report an error as tuple is immutable

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4.

# Strings are immutable to ensure memory efficiency,security ,and  performance.
# when we modify string a new string object is created,and the variable points to the new object.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5.

s = "Python"
print(id(s))       # 2391635591456
s = s + "3"
print(id(s))       # 2391636004848
#two different addresses are created coz strings are immutable so performing operations create a new object


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6.

# A dictionary is a collection of key–value pairs used to store data efficiently.
# Key–value pair:Each key maps to a value(name:"Amar")
# Why keys must be immutable: To ensure consistent hashing
# Why duplicate keys are not allowed: Each key must be unique to avoid ambiguity nd duplicate keys overwrite old values

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7.

d = {1: "One", 1: "ONE", 2: "Two"}
print(d)                                       #Output: {1: 'ONE', 2: 'Two'}
#Dictionary keys must be unique.The second value for key 1 overwrites the first one.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8.

# range is an immutable sequence type used to generate a sequence of numbers.
# difference between list and range is that list stored the elements,whereas range genetares elements

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 9.

r = range(5)
print(r)                       # range(0, 5)
print(list(r))                 # [0, 1, 2, 3, 4]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 10. 
 
range(1, 10)                      # range(start,stop) → starts from 1,stop at 9,step = 1(move forward by 1)
range(1, 10, 2)                   # range(start, stop, step) → starts from 1,stop at 9,step = 1 (increments by 2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
