def bubble_sort(arr):
    for x in range(len(arr)):
        for j in range(0,len(arr)-x-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
bubble_sort([23,54,87,100,28,64,83,32])
