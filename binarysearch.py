def binary(arr,key):
    
    n = len(arr)
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] < key:
            l = mid + 1
        elif arr[mid] > key:
            r = mid - 1
        else:
            return mid
    return -1
arr = [1,2,3,6,34,45,100]
key = 45
print(binary(arr,key))