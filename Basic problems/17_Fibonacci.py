n=int(input("Enter number of terms\n"))
a=0
b=1
print(a, b,end=' ')
for j in range(1,n-1):
c = a+b
print(c)
a,b=b,c
