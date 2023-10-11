# Python program for the ternary search algorithm:

# Function to perform Ternary Search:
def ternarySearch(l, r, key, ar):
     
    if (r >= l):
        # Finding 2 midpoints(Ternary Search so we split the array into 3):
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
      
        # If the target is present at any midpoint:
        if (ar[mid1] == key): 
            return mid1
        if (ar[mid2] == key): 
            return mid2

        # Repeat Search operation and check if the element is in any of the 2 midpoints:
        if (key < ar[mid1]): 
            # Target between leftmost element and midpoint 1:
            return ternarySearch(l, mid1 - 1, key, ar)
         
        elif (key > ar[mid2]): 
            # Target between midpoint 2 and rightmost element
            return ternarySearch(mid2 + 1, r, key, ar)
         
        else: 
            # Target betwen the 2 midpoints:
            return ternarySearch(mid1 + 1, mid2 - 1, key, ar)
  
    # Key not found
    return -1

# Sorted Array where we search for key:
arr = [10, 21, 35, 47, 52, 58, 76, 81, 92, 96]
target = 35

# Search the key using ternarySearch
p = ternarySearch(0, len(arr)-1, target, arr)
 
# Print the result
print("Index of", target, "is", p)
