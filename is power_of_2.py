def isPowerOfTwo (x):
 
    # First x in the below expression
    # is for the case when x is 0
    return (x and (not(x & (x - 1))) )
  
n=int(input("Enter a number"))
if(isPowerofTwo(n)):
  print(n+"is a power of 2")
else:
  print(n+"is not a power of 2")
    
