student_record = {
    'name': 'John Doe',
    'year': 2023,
    'scores': {
        'math': 85,
        'english': 92,
        'science': 78,
        'history': 88
    },
    'contact': {
        'email': 'john.doeexample.com',
        'phone': '123-456-7890'
    }
}

subject_total = sum(student_record['scores'].values())

has_email = '@' in student_record['contact']['email']

print(f"Subject Total: {subject_total}")
print(f"Has Email: {has_email}")
