def linear(arr,key):
    for i in range(len(arr)):
        if arr[i] != key:
            i = i + 1
        else:
            print("The key is at index ",i)
    return -1

arr = [3,44,56,77]
key = 56
linear(arr,key)