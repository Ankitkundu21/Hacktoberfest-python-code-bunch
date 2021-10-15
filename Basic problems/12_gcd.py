x=int(input("Enter a number\n"))
y=int(input("Enter a number\n"))


if(x>y):
    min=y
else:
    min=x

for i in range(1,min+1):
    if ((x%i==0) and (y%i==0)):
        gcd=i
        lcm=(x*y)/gcd
print(gcd)
print(lcm)