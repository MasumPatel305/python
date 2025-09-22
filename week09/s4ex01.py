def insertion_sort(unsorted):
    sorted_list = []
    for value in unsorted:
        smaller = [v for v in sorted_list if v < value]
        index = len(smaller)
        sorted_list.insert(index, value)
    return sorted_list

nums = [9, 8, 7, 6]
sorted_nums = insertion_sort(nums)
print(sorted_nums)
