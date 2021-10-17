k=(input("Enter three number\n"))
x=k.split(" ")

if(x[0]>=x[1] and x[0]>=x[2]):
    print("A is greater")

elif(x[1]>=x[0] and x[1]>=x[2]):
    print("B is greater")

else:
    print("C is greater")
