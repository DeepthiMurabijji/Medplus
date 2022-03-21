'''
# palindrome of number 
n=int(input("enter the number: "))
x=n
r=0
while(n>0):
	z=n%10
	r=r*10+z
	n=n//10
if(x==r):
	print("number is palindrome")
else: 
	print("number is not a palindrome")
	


# palindrome of a string 
a=input("enter a string: ")
if(a==a[::-1]):
	print("the string is palindrome")
else:
	print("the is not a palindrome")
	
'''
# another method of string palindrome 
str=input("enter a string: ")
x=str.casefold()
r=reversed(str)
if list(str)==list(r):
	print("PALINDROME")
else:
	print("NOT PALINDROME")
	
