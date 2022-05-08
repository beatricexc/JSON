import json
student = {
    "first_name": "Jane",
    "last_name": "Allred"
}
json_data = json.dumps(student, indent=2)
print(json_data)
print(json.loads(json_data))
