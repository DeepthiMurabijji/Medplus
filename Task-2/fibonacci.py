n=int(input("enter the value: "))
a=0; b=1;c=0;
if(n<=0):
	print("NO negative values!")
elif(n==1):
	print(a)
else:
	for i in range(1,n):
		c=a+b
		a=b
		b=c
		print(b,end=" ")
