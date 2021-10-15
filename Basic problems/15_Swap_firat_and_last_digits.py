x=int(input("Enter the Number:- "))
count=0
temp=x
while(temp>0):
    count+=1
    temp=int(temp/10)
print(count)

ld=x%10
fd=int(x/(10**(count-1)))
print(ld)
print(fd)

newnum = ld*(10**(count-1))
newnum = newnum + fd
y=int(x/10)
y=int(y%(10**(count-2)))
print(y)
newnum=newnum+(y*10)
print(newnum)