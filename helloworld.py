student = {
    "name": "Mark",
    "student_id": 13123,
    "feedback": None
}

try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding last name")

print("This code executes")