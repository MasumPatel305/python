import json

def to_json(data):
    return json.dumps(data)

def from_json(s):
    return json.loads(s)

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
        'email': 'john.doe@example.com',
        'phone': '123-456-7890'
    }
}

json_string = to_json(student_record)
print(json_string)

restored_data = from_json(json_string)
print(student_record == restored_data)
