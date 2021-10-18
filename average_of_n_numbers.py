n=int(input("Enter limit for which you want to calculate average"))
li=[]
sum=0
print("Give input of n numbers")
for i in range(n):
  b=int(input())
  li.append(b)
  
for i in range(n):
  sum=sum+li[i]
  
print("Average of numbers:-"+ sum/n)
