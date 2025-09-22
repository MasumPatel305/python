# 3. Use .copy() to clone a list and prove changes don't affect the original.
fruits = ["apple","banana"]

a = fruits.copy()

a[0] = "orange"

print(fruits)
print(a)
