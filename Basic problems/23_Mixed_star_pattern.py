n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")

for i in range(n,-1,-1):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")