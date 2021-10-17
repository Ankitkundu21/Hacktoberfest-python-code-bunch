def isArmstrong(x): 
    n = order(x) 
    temp = x 
    sum1 = 0     

    while (temp != 0): 
        r = temp % 10
        sum1 = sum1 + power(r, n) 
        temp = temp // 10

    return (sum1 == x) 
  
x = 153
print(isArmstrong(x)) 

x = 1253
print(isArmstrong(x)) 
