def sel_sort(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        c=0
        for j in range(i+1, len(arr)):
            if min>arr[j]:
                min=arr[j]
                n=j
                c=1
#                 print(c)
        if c==1:
            arr[i], arr[n]=min, arr[i]
#         print(arr)
    return arr
arr=[15, 4, 7, 18, 1]
sel_sort(arr)