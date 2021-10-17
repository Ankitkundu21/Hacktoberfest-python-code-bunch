sum=0
n=int(input("Enter a number\n"))

#1/2 + 1/3 +...
# for i in range(2,n+1):
#     sum=sum+(1/i)
# print(sum)

# 1+ 1/4 + 1/9+...
# for i in range(1,n+1):
#     sum=sum+(1/(i*i))
# print(sum)

#1+(1+2)+(1+2+3)
for i in range(1,n+1):
    sum=sum+(i*(i+1)/2)
print(sum)