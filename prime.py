'''
def prime(a):
	if(a>1):
		for i in range (2,int(a/2)+1):
			if(a%i==0):
				print(a,"is not a prime number")
				break
			else:
				print(a,"is a prime number")
				break
	else:
		print(a,"is not a prime number")
a=int(input("enter the value: "))
prime(a)

'''
# range of prime numbers
l=int(input("enter the start value: "))
u=int(input("enter the end value: "))
for i in range(l,u+1):
	if(i>1):
		for j in range(2,i):
			if(i%j==0):
				break
		else:
			print(i,end=" ")		
