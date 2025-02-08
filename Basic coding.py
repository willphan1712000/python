# n=input('enter a number: ')
# m=int(n)
# while m>0:
#    if m==3:
#        break
#    print(m)
#    m=m-1
# print('all done')
# print(m)

# Finding smallest and largest
# smallest=99
# print('Before',smallest)
# for matrix in [43,56,28,93,94,]:
#    if matrix<smallest:
#        smallest=matrix
#    print(matrix,smallest)
# print('The smallest number is',smallest)

# Summing
#value = 0
#for thing in [2,34,64,78,45,23]:
#    value=value+thing
#print('Sum',value)

# Enter numbers and find the smallest and largest nubmer
#largest = 0
#smallest = 99
#matrix = []
#while True:
#    inp = input("Enter a number: ")
#    if inp == "done" : break
#    else:
#        matrix.append(inp)
#print(matrix)
#for num in matrix:
#    try:
#        nu=int(num)
#        if nu>largest:
#            largest=nu
#        if nu<smallest:
#            smallest=nu
#    except:
#        print ("Invalid input")
#print ("Maximum is", largest)
#print ("Minimum is", smallest)

# Strings
#string='willphan'
#count=0
#while count<len(string):
#    print(count, string[count])
#    count=count+1
#print('there are',len(string),'letters of string')

# Finding in string
# data=input('Enter your BK account: ')
# a=data.find('@')
# b=data.find('.')
# print(b)
# c=data.find('.',b+1)
# print(c)
# h=data[a+1:c]
# print ('The host is: ', h)

# Iteration with two variables
#t=[2,4,5,6]
#u=[1,2,3,4]
#for i, j in zip(t, u):
#    print(i, j)

# import numpy as np
# from numpy import linspace
# import sympy as sym
# import math
# L=[1, 5, 1/3]
# L1=np.array(L)
# print(L1)

#file=open('Python.txt')
#count = 0
#for line in file:
#    line=line.rstrip() #if there is no this syntax of rstrip, 
    #the "print statement" adds a newline of whitespace between two lines from the file
#    count = count + 1
#    print(line)
#print('there are',count,'lines in the file',file)

# WRITE DATA TO EXCEL FILE (XLSX)
#import xlsxwriter
#workbook = xlsxwriter.Workbook('c:\\Users\\DELL\\Desktop\\Welocme.xlsx')
#worksheet = workbook.add_worksheet()
#worksheet.write('A1', 'Welcome to Python')
#workbook.close()
# ANOTHER WAY TO WRITE XLSX FILE
#import pandas as pd
#array = [['a1', 'a2', 'a3'],
#         ['a4', 'a5', 'a6'],
#         ['a7', 'a8', 'a9'],
#         ['a10', 'a11', 'a12', 'a13', 'Nh']]
#df = pd.DataFrame(array)
#df.to_excel(excel_writer = "C:/Users/DELL/Desktop/test.xlsx")

# DICTIONARY
#A = dict()
#A['N'] = 1
#A['B'] = 2
#print(A)
# Counting in dictionary
#counts = dict()
#names = ['N', 'T', 'K', 'K', 'N', 'N', 'K', 'T', 'N']
#for name in names:
#    if name not in counts:
#        counts[name] = 1
#    else:
#        counts[name] = counts[name] + 1
#print(counts)
# Counting with simplified method 'get'
#counts = dict()
#names = ['N', 'T', 'K', 'K', 'N', 'N', 'K', 'T', 'N']
#for name in names:
#    counts[name] = counts.get(name, 0) + 1
#print(counts)
# Get method means when the key is already in the dictionary, its value is added to the following
#value. When the key is not, its value is designated to the default value


import numpy as np
 
# Taking a 3 * 3 matrix
E2 = np.array([[2, 0, 1, 3, -2], [-2, 1, 3, 2, -1], [1, 0, -1, 2, 3], [3, -1, 2, 4, -3], [1, 1, 3 ,2, 0]])
E3 = np.array([[2, 1, 3, -2], [0, 6, 4, -7], [0, -3, 1, 8], [4, 5, 6, -3]])
E4 = np.array([[-11, -5, 12], [6, 4, -7], [9, -2, -15]])
det = np.linalg.det(E4)
 
# Calculating the inverse of the matrix
print(round(det))

# E1 = np.array([[1, 0],
#               [1, -3]])
# E1in = np.linalg.inv(E1)
# E2 = np.array([[1, -1],
#               [0, 1]])
# E2in = np.linalg.inv(E2)
# E3 = np.array([[1/3, 0],
#               [0, 1]])
# E3in = np.linalg.inv(E3)
# E4 = np.array([[1, 0],
#               [0, -1/2]])
# E4in = np.linalg.inv(E4)
 
# # Calculating the inverse of the matrix
# print(E1in @ E2in @ E3in @ E4in)