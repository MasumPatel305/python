# 1. Sort [5, 1, 4, 2] using selection_sort.

a = [5,1,4,2]

def selection_sort(unsorted):
    sorted_list=[]
    while unsorted:
        minimum = min(unsorted)
        sorted_list.append(minimum)
        unsorted.remove(minimum)
    return sorted_list

print(selection_sort(a))