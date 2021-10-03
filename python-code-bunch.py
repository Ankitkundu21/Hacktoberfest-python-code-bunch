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
