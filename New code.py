#Swap elements based on position:

list=[62,12,8,76]
def newlist(list):
    list[1],list[2]= list[2], list[1]
    return list
print(newlist(list))
