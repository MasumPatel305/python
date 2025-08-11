# Section 11: Refactoring

# Bad nested structure
# age = 25
# cost = 9
# if age > 21:
#     if cost < 10:
#         print("Buy")
#     else:
#         print("Too expensive")
# else:
#     print("Too young")

# # Better
# if age <= 21:
#     print("Too young")
# elif cost < 10:
#     print("Buy")
# else:
#     print("Too expensive")

# Exercise 11:
# Write a nested if-else structure and then refactor it into a cleaner version


temperature = 30
is_raining = False

if temperature <= 25:
    print("Too cold")
elif is_raining:
    print("Stay indoors")
else:
    print("Go for a walk")
