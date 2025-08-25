total = 0
trace = 0  

lst = [3, 5, -2, 4]

for item in lst:
    trace = total
    total += item
    print(f"The total was {trace}, after adding {item}, the total is {total}")