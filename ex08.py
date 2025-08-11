# Section 8: List of Dictionaries

people = [
    {"name": "Arjun", "age": 18},
    {"name": "Allira", "age": 36}
]

# Print all names
# for person in people:
#     print(person["name"])

# Exercise 8:
# Write a function to return the average age from a list of such dictionaries

result = 0
n = 0

for person in people:
    n +=1
    result += person['age'] 

final_result = result/n

print(final_result)