def count_occurrences(lst, target):
    total = 0
    for n in lst:
        if n == target:
            total +=1
    
    return total

print(count_occurrences([1, 2, 3, 1, 4, 1], 1))  
