# import math
# n=int(input("Enter Range\n"))
# x=int(input("Enter angle\n"))
# x=(x*(3.14/180))
# sum=1
# for i in range(n):
#     sign=(-1)**i
#     sum+=((x**(2*i))/math.factorial(2*i))*sign
# print(sum)

n=int(input("Enter Range\n"))
x=int(input("Enter angle\n"))
x=(x*(3.14/180))
sum=1
sign=-1
fact=1
a=1
count=1
for i in range(2,(2*n),2):
    fact=fact*i*(i-1)
    print(fact)
    a=(sign**count)*(pow(x,i))
    count+=1
    sum=sum+(a/fact)
print(sum)