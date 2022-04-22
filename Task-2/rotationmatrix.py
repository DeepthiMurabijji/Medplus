'''
def matrix(a):
	n=len(a[0])
	for i in range(n//2):
		for j in range(i, n-i-1):
			t=a[i][j]
			a[i][j] = a[n-1-j][i]
			a[n-1-j][i] = a [n-1-i][n-1-j]
			a[n-1-i][n-1-j] = a [j][n-1-i]
			a[j][n-1-i]=t

a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]	
  '''
import numpy as np

r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))


a=[[int(input()) for i in range (c)] for j in range(r)]

for i in range(r):
	for j in range(c):
		print(a[i][j],end=" ")
	print() 


matrix(a)
n=len(a[0])
for i in range(n):
	print(a[i])
	
'''
print("Enter the entries in a single line (separated by space): ")
  

entries = list(map(int, input().split()))
  
# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix)	
'''	
