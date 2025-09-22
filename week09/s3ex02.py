# 2. Try it on an already sorted list. What happens?
def selection_sort_inplace(lst):
    for i in range(len(lst)):
        min_val = min(lst[i:])
        min_i = lst.index(min_val, i)
        lst[i], lst[min_i] = lst[min_i], lst[i]
    return lst

nums = [1, 5, 8, 12]
sorted_nums = selection_sort_inplace(nums)
print(sorted_nums)
