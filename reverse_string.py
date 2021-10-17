#Reverse a string

input='Good morning guys'
def rev_string(input): #Function For Reverse string
    words=input.split(' ')
    reverse_string= " ".join(reversed(words))
    return reverse_string
def string(input): #Function For Particular No Position
    n=3
    posi=input.split(' ')[n-1]
    print("Word of",n,"no position is : ",posi)
print(rev_string(input))
string(input)
