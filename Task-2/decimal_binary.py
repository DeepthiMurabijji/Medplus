#Decimal to binary !!!


'''
def dec_to_bi (n):
    if( n > 1 ):
        dec_to_bi(n//2)
    print(n%2,end=" ")
if __name__=='__main__':
    dec_to_bi(8)
    print("\n")
    dec_to_bi(18)
    print("\n")
    dec_to_bi(7)
    print("\n")



x=255
print(x/2)
print(x//2)
print(x%2)


n=(input("enter the value: "))
binary=bin(int(n)).replace("0b","")
print("The decimal number is: ",binary)
    
'''
def decimaltobinary(x):
    if (x>1):
        decimaltobinary(x//2)
    print(x%2, end=" ")
x=int(input("enter the value: "))
decimaltobinary(x)
    
    
    
