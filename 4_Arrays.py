"""1. Write a function to add integer values of an array"""

print("----------------perform sum of integers in array--------------")
x = [1,2154,5,6,7,8,9,4,6]
s = 0
for i in x:
    s += i
print(s)
#print(sum(x))
"""2. Write a function to calculate the average value of an array of integers
"""
print("\n----------------perform average of integers in array--------------")
average = s/(len(x))
print(average)

"""3. Write a program to find the index of an array element"""
# find 2154 in 'x' array
print(x)
print("\n----------------finding element index in array--------------")
y = eval(input("Input the array element: "))
def index_e(x,y):
    for i in range(len(x)):
      if x[i] == y:
        print(i,"is the index position of element in the array")
index_e(x,y)

"""4. Write a function to test if array contains a specific value"""
print("\n----------------finding element existence in array--------------")
y = eval(input("Input the array element to check existence: "))
def test_exist(x,y):
    if y in x:
        print('True',"element exists in the array")
    else:
        print('False',"element does not exists in the array")
test_exist(x,y)

"""5. Write a function to remove a specific element from an array"""
print("\n----------------removing element from the array--------------")
print(x)
r = eval(input("Input the array element to delete: "))
def remove_e(x,r):
    if r in x:
        x.remove(r)
        print("Performing delete operation...\n",x)
    else:
        print("The element does not exists in the array")
remove_e(x,r)

"""6. Write a function to copy an array to another array"""
print("\n----------------copy array to another array--------------")
array = x.copy()
print("Copied x to array",array)
