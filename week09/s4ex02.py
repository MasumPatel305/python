def insertion_sort(unsorted):
    sorted_list = []
    insertions = 0   
    for value in unsorted:
        smaller = [v for v in sorted_list if v < value]
        index = len(smaller)
        sorted_list.insert(index, value)
        insertions += 1  
    return sorted_list, insertions

nums = [9, 8, 7, 6]
sorted_nums, num_insertions = insertion_sort(nums)
print("Sorted List:", sorted_nums)
print("Number of Insertions:", num_insertions)
