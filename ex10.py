# Section 10: Tracing Code

# Tracing values of variables
# count = 0
# count += 3
# count += 2
# print("Final count:", count)

# Exercise 10:
# Trace the value of a variable modified in an if-else block based on user input (use input())

score = 0
print("Initial score:", score)

answer = input("Enter 'yes' or 'no': ").strip().lower()

if answer == "yes":
    score += 10
    print("You entered YES — score increased to:", score)
else:
    score -= 5
    print("You entered NO or something else — score decreased to:", score)

print("Final score:", score)