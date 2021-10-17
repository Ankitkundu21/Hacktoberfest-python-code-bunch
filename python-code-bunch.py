#Q1:SUM OF DIGITS [USING append()]

#SOLUTION :
digits=[]
sum=0
for i in range(21):
     digits.append(i)
for i in digits:
     sum+=i       
print(digits)
print("Sum of digits is : ", sum)

#Q2: CHECK EVEN NUMBERS BETWEEN CERTAIN RANGE OF VALUE 
#SOLUTION :
def check(x):
    if(x % 2 == 0 or x % 4 == 0):
        return x
evens=list(filter(check, range(2,30)))
print(evens)
         
#Q3:FIND THE SECOND LARGEST NUMBER (LIST)
#SOLUTION
digits=[]
value = (int(input("Number of element you wanna insert : ")))
for i in range(1, value + 1):
    item = int(input("Enter the no-{} element: ".format(i)))
    digits.append(item)
digits.sort()
print("Second largest number is : " , digits[-2])

#Count the No Of Vowel in a String
#solution:
n=input('enter a value')
c= 0
v='aeiouAEIOU'
for i in n:
   if i in v:
        c = c+1
print (c)
