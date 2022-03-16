def binary(arr,x):
	low=0
	high=len(arr)-1
	mid=0
	while(high>=low):
		mid=(high+low)//2
		if(arr[mid]<x):
			low=mid+1
		elif(arr[mid]>x):
			high=mid-1
		else:
			return mid
	return -1
arr=[1,4,5,6,9,17,32]
x=int(input("search for : "))

result=binary(arr,x)
if(result != -1):
	print(str(result))
else:
	print("No such element")
	
'''
n=int(input("No.of Elements in array: "))
a= list(map(int,input("elements of array: ")strip.split()))


a=[]
n=int(input("No.of elements in array: "))
for i in range(0,n):
	l=int(input())
	a.append(l)
print(a)

'''

