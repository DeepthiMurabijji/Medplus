def search(arr,x):
	for i in range(len(arr)):
		if(arr[i]==x):
			return i
	return -1
	
n=int(input("No.of Elements in array: "))
a= list(map(int,input("elements of array: ").strip().split()))
x=int(input("search for: "))
r=search(a,x)
if(r==-1):
	print("Element not found")
else:
	print("Element is at: ",r)

