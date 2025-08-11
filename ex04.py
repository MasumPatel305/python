# Section 4: Nested Loops
# Example of nested loop with 2D list

# pattern = [
#     ['*', '*', '*'],
#     ['*', ' ', '*'],
#     ['*', '*', '*']
# ]

# for row in pattern:
#     for ch in row:
#         print(ch, end="")
#     print()



a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

highest = max(max(i) for i in a)

print("Maximum value:", highest)
