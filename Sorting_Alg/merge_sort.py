def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    
    left_arr=merge_sort(arr[:mid])
    right_arr=merge_sort(arr[mid:])
    
    return merge(left_arr, right_arr)
def merge(left, right):
#     print(left)
#     print(right)
    merge_arr=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merge_arr.append(left[i])
            i+=1
        else:
            merge_arr.append(right[j])
            j+=1
#     print(merge_arr)
    while i<len(left):
        merge_arr.append(left[i])
        i+=1
    while j<len(right):
        merge_arr.append(right[j])
        j+=1
        
#     print(merge_arr)
    return merge_arr

arr=[1, 3, 2, 1, 2, 6, 0, 9]
merge_sort(arr)