def partition(arr,low,high):
    tmp = arr[low]
    pivotkey = arr[low]
    while low<high:
        while low<high and arr[high]>=pivotkey:
            high = high - 1
        arr[low] = arr[high]
        while low<high and arr[low]<=pivotkey:
            low = low + 1
        arr[high] = arr[low]
    arr[low]=tmp
    print(arr)
    return low
def qsort(arr,low,high):
    if low<high:
        pivotloc = partition(arr,low,high)
        qsort(arr,low,pivotloc-1)
        qsort(arr,pivotloc+1,high)

arr = [49,38,65,97,76,13,27,49]
print(arr)
qsort(arr,0,len(arr)-1)

print(arr)
