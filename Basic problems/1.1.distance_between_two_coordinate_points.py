import math

a= input("Enter the value of x1, y1 ")
p1=a.split(",")
b= input("Enter the value of x2, y2 ")
p2=b.split(",")

distance= math.sqrt((int(p1[0])-int(p2[0]))**2+(int(p1[0])-int(p2[0]))**2)
print(distance)