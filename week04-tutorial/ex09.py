students = {"Alice": 88, "Bob": 92, "Charlie": 92, "Diana": 85}
def topper(data):
    highest_score = max(data.values())

    ranker = [name for name, score in data.items() if score == highest_score]

    return ranker

print(topper(students))