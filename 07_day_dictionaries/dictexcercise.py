# Create an empty dictionary called dog
dog = {}
print(dog)  # {}    
# Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Buddy', 'color': 'Brown', 'breed': 'Golden Retriever', 'legs': 4, 'age': 3}
print(dog)  # {'name': 'Buddy', 'color': 'Brown', 'breed': 'Golden Retriever', 'legs': 4, 'age': 3}
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'gender': 'Female',
    'age': 22,
    'marital_status': False,
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': {
        "street": "123 Main St",
        "zipcode": "10001"
    }
}
print(student)  # {'first_name': 'Alice', 'last_name': 'Smith', 'gender': 'Female', 'age': 22, 'marital_status': False, 'skills': ['Python', 'JavaScript'], 'country': 'USA', 'city': 'New York', 'address': {'street': '123 Main St', 'zipcode': '10001'}}     

# Get the length of the student dictionary
print(len(student))  # 9
# Get the value of skills and check the data type, it should be a list
print(student['skills'])  # ['Python', 'JavaScript']
print(type(student['skills']))  # <class 'list'>
# Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')
print(student['skills'])  # ['Python', 'JavaScript', 'HTML', 'CSS']
# Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list)  # ['first_name', 'last_name', 'gender', 'age', 'marital_status', 'skills', 'country', 'city', 'address']
# Get the dictionary values as a list
values_list = list(student.values())
print(values_list)
# Change the dictionary to a list of tuples using items() method
items_list = list(student.items())
print(items_list)  # [('first_name', 'Alice'), ('last_name', 'Smith'), ('gender', 'Female'), ('age', 22), ('marital_status', False), ('skills', ['Python', 'JavaScript', 'HTML', 'CSS']), ('country', 'USA'), ('city', 'New York'), ('address', {'street': '123 Main St', 'zipcode': '10001'})]

# Delete one of the items in the dictionary
del student['marital_status']
print(student)  # {'first_name': 'Alice', 'last_name': 'Smith', 'gender': 'Female', 'age': 22, 'skills': ['Python', 'JavaScript', 'HTML', 'CSS'], 'country': 'USA', 'city': 'New York', 'address': {'street': '123 Main St', 'zipcode': '10001'}}

# Delete one of the dictionaries
#del dog
#print(dog)  # NameError: name 'dog' is not defined
#del student
#print(student)  # NameError: name 'student' is not defined 