import math
#Enter Input
number = input('Enter the number:')
# Function to calculate digital root of number
def digitalRoot(number):
    # If number is 0 return 0
    if (number == "0"):
        return 0
    # Count sum of digits under mod 9
    ans = 0
    for i in range (0, len(number)):
        ans = (ans + int(number[i])) % 9
    # If digit sum is multiple of 9, answer 
    # 9, else remainder with 9.
    if(ans == 0):
        return 9
    else:
        return ans % 9
print ('Digital Root:'+str(digitalRoot(number)))
