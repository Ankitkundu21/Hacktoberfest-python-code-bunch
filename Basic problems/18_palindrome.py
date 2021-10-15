n=int(input())
temp=n
Reverse = 0
while (n > 0):
    rem = n % 10
    Reverse = (Reverse * 10) + rem
    n = n // 10
if(temp==Reverse):
    print("Is a Palindrome\n")
else:
    print("Not a palindrome\n")