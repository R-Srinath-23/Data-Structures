def quick_sort(arr):
    
    if len(arr)<=1:
        return arr
    p=arr[0]
    lift_arr=[]
    right_arr=[]
    for i in range(1, len(arr)):
        if arr[i]<p:
            lift_arr.append(arr[i])
        else:
            right_arr.append(arr[i])
    
    return quick_sort(lift_arr)+[p]+quick_sort(right_arr)
    
ls=[1, 3, 4, 2, 1]
quick_sort(ls)