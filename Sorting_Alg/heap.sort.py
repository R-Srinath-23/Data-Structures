def heap_max(arr):
#     print(arr)
    if len(arr)<=1:
        return arr
    if len(arr)>2:
#         return heap_sort(arr)
        n=len(arr)//2
        for i in range(len(arr)):
            if i<n:
                if i==0:
                    if arr[i]<arr[i+1] or arr[i]<arr[i+2]:
                        if arr[i+1]<arr[i+2]:
                            arr[i], arr[i+2]=arr[i+2], arr[i]
                        else:
                            arr[i], arr[i+1]=arr[i+1], arr[i]
#                     print(arr)
                else:
                    if i+2<len(arr) and i+3<len(arr):

                        if arr[i]<arr[i+2] or arr[i]<arr[i+3]:
                            if arr[i+2]<arr[i+3]:
                                arr[i], arr[i+3]=arr[i+3], arr[i]
                            else:
                                arr[i], arr[i+2]=arr[i+2], arr[i]
#                     print(arr)
    
#     print(arr)
    arr[0], arr[-1]=arr[-1], arr[0]
    return heap_max(arr[:-1])+[arr[-1]]
#     if c==0:
#     return heap_sort(arr)
# #     else:
# #         return heap_max(arr)
    
# def heap_sort(arr):
#     arr[0], arr[-1]=arr[-1], arr[0]
#     print(arr)
#     return heap_max(arr[:-1])

arr=[4, 10, 3, 5, 1, 6, 7, 1]
heap_max(arr)