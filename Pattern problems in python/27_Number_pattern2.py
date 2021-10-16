n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(2,i+1,1):
        print(j,end=" ")
    print("\n")