def bubble(arr):
    n = len(arr)
    for i in range (n):
        state = False

        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                state = True
        print("After the ",i,"the swap",arr)
        if (state == False):
            break
arr = [3,7,8,6,3,4]
bubble(arr)
print("The sorted array is ",arr)