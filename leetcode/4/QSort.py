#coding:utf-8
# 快排内容参考blog  https://www.jianshu.com/p/5cf4d40f9aaa 其中有两种partitiono的写法
def Partition(arr,low,high):
    # 设置起始点
    # 这里选择第一个为起始点
    pivotkey = arr[low]
    tmp = arr[low]
    # 循环 找到中位数
    while low < high:
        # 在low<high的时候，
        while low < high and arr[high] >= pivotkey:
            high = high - 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivotkey:
            low = low + 1
        arr[high] = arr[low]
    arr[low] = tmp
    return low
def QSort(arr,low,high):
    if low<high:
        mid = Partition(arr,low,high)
        QSort(arr,low,mid-1)
        QSort(arr,mid+1,high)

arr = [49,38,65,97,76,13,27,49]
QSort(arr,0,len(arr)-1)

print(arr)

