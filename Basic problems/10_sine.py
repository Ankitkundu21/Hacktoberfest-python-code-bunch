import math

n=int(input("Enter Range\n"))
x=int(input("Enter angle in radians\n"))

sine=0
for i in range(n):
    sign=(-1)**i
    y=(x*(3.14/180))
    sine+=((y**(2.0*i+1))/math.factorial(2*i+1))*sign

print(sine)
