def selection_sort_by_age(unsorted):
    unsorted = unsorted[:] 
    sorted_list = []
    
    while unsorted:
        m = min(unsorted, key=lambda x: x['age'])
        
        sorted_list.append(m)
        
        unsorted.remove(m)
    
    return sorted_list

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 25},
    {"name": "David", "age": 35}
]

sorted_people = selection_sort_by_age(people)
print(sorted_people)
