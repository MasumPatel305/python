import random

roll_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(10):
    roll = random.randint(1,6)
    roll_counts[roll]+=1

for face, count in roll_counts.items():
    print(f"Face: {face}:{count} times")