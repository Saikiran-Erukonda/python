# 2.OPERATORS
"""
1. Write a function for arithmetic operators(+,-,*,/)
"""

#we need to give the 2 numbers as input and the respective outputs will be displayed after arithmetic operations

i_a = eval(input("enter first number: "))
i_b = eval(input("enter second number: "))
print("The two numbers are","\ni_a =",i_a,"\ni_b = ",i_b)
print("o_addition =", i_a + i_b)
print("o_subtraction =",i_a - i_b)
print("o_multiplication =", i_a * i_b)
print("o_division = ",i_a/i_b)

""" 2. Write a method for increment and decrement operators(++, --) """
# python does not have increment and decrement operator directly. Use for loop for increment and decrement operations
i = 0
k = 20
for i in range(0,5):
  print(i)  # prints value of i upto 4
for k in range(20,15,-1):
  print(k)  # prints value of k upto 16


""" 3. Write a program to find the two numbers equal or not."""


value = 100
number = 100
print("\nvalue = ",value,"\nnumber = ",number)
print("Is the value equal to number :",value == number)


""" 4. Program for relational operators (<,<==, >, >==)"""

value1 = 100
number1= 120
print("\nvalue1 = ",value1,"\nnumber1 = ",number1)
print("Is the value1 equal to number1: ",value1 == number1)                    #value1 == number1
print("Is the value1 less than number1: ",value1 < number1)                    #value1 < number1
print("Is the value1  less than or equal to number1 :",value1 <=  number1)     #value1 <= number1
print("Is the value1 greater than number1 :",value > number)                   #value1 > number1
print("Is the value1 greater than or equal to number1: ",value1 >= number1)    #value1 >= number1

"""
5. Print the smaller and larger number
"""

a = eval(input('Enter first number: '))
b = eval(input('Enter second number: '))
#To print larger number
if a > b: 
     print(a, "is larger ")
else:
    print(b, " is larger ")
#To print smaller number
if a < b:
     print(a, "is smaller ")
else:
    print(b, " is smaller ")  

