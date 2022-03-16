def binarytodecimal (n):
    i=0;r=0
    while(n>0):
        d=n%10
        r=r+d*pow(2,i)
        n=n//10
        i=i+1
    print(r)
n=int(input("enter the value: "))
binarytodecimal(n)
