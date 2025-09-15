# 10. Make two dicts and update one with the other. Observe changes.

a =  {"name": "Messi", "age": 25}
b = {"age": 26, "city": "New York"}

a.update(b)

print(a)