def bubble_sort(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j], list1[j+1]=list1[j+1], list1[j]
    return list1
list1=[2, 5, 4, 3, 1]
bubble_sort(list1)