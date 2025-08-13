def insert_sort(arr):
    for i in range(len(arr)):
        if i<len(arr)-1:
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1]=arr[i+1], arr[i]
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1]=arr[j-1], arr[j]
    return arr

arr=[2, 4, 3, 1, 1]
insert_sort(arr)