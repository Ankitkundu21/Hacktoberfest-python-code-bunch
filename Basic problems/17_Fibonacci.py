n=int(input("Enter number of terms\n"))
a=0
b=1
c=0
if n<=0:
    print("Enter only positive numbers")
elif(n==1):
    print(a)
else:
    while(c<n):
        print(a,end=" ")
        x=a+b
        a=b
        b=x
        c=c+1