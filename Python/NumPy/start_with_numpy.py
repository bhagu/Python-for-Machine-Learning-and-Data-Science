import numpy as np

mylist = [1,2,3]

print(mylist)
print(type(mylist))

myarr = np.array(mylist)

print(myarr)
print(type(myarr))

my_matrix = [[1,2,3], [4,5,6], [7,8,9]]

print(my_matrix)

print(np.array(my_matrix))

print(np.arange(0,10))

print(np.arange(0,10,2))

print(np.zeros(10))

print(np.zeros((5,5)))

print(np.ones(10))

print(np.ones((4,4)))

print(np.linspace(0,10,10))