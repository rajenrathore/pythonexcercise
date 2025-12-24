# dictionaries.py
#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

#Creating a Dictionary
#We can create a dictionary by placing a comma-separated sequence of key:value pairs within curly {} brackets {}. 
#Keys must be unique and immutable (cannot be changed) data types such as strings, numbers or tuples. 
#Values can be of any data type and can be duplicated.  
# empty dictionary
empty_dict = {}
print(empty_dict)  # {}
# dictionary with string keys and values of different data types
person = {'name': 'John', 'age': 30, 'is_student': False}
print(person)  # {'name': 'John', 'age': 30, 'is_student': False}   
# dictionary with mixed keys
mixed_dict = {1: 'apple', '2': 'banana', (3, 4): 'cherry'}
print(mixed_dict)  # {1: 'apple', '2': 'banana', (3, 4): 'cherry'}  
#Creating a dictionary using dict() method
dict_from_list = dict([(1, 'apple'), (2, 'banana'), (3, 'cherry')])
print(dict_from_list)  # {1: 'apple', 2: 'banana', 3: 'cherry'} 
# dictionary from keyword arguments
dict_from_kwargs = dict(name='Alice', age=25, city='New York')
print(dict_from_kwargs)  # {'name': 'Alice', 'age': 25, 'city': 'New York'} 

#Accessing Dictionary Items
#We can access dictionary items by referring to its key name inside square brackets [] or by using the get() method.
person = {'name': 'John', 'age': 30, 'is_student': False}
print(person['name'])  # 'John'
print(person.get('age'))  # 30
#Trying to access a non-existing key
#print(person['address'])  # KeyError
print(person.get('address'))  # None    


#dictionary length
print(len(person))  # 3 

#adding dictionary items

person['address'] = '123 Main St'
print(person)  # {'name': 'John', 'age': 30, 'is_student': False, 'address': '123 Main St'}
person.update({'phone': '555-1234'})
print(person)  # {'name': 'John', 'age': 30, 'is_student': False, 'address': '123 Main St', 'phone': '555-1234'}    

#Modifying Dictionary Items
person['age'] = 31
print(person)  # {'name': 'John', 'age': 31, 'is_student': False, 'address': '123 Main St', 'phone': '555-1234'}
person.update({'is_student': True})
print(person)  # {'name': 'John', 'age': 31, 'is_student': True, 'address': '123 Main St', 'phone': '555-1234'} 

#Checking Keys in a Dictionary
print('name' in person)  # True
print('gender' in person)  # False

#Removing Dictionary Items
del person['phone']
print(person)  # {'name': 'John', 'age': 31, 'is_student': True, 'address': '123 Main St'}
age = person.pop('age')
print("Removed age:", age)  # Removed age: 31
print(person)  # {'name': 'John', 'is_student': True, 'address': '123 Main St'}
is_student = person.popitem()
print("Removed item:", is_student)  # Removed item: ('is_student', True)    
print(person)  # {'name': 'John', 'address': '123 Main St'} 

#Changing Dictionary to a List of Items
#The items() method changes dictionary to a list of tuples.
items_list = list(person.items())
print(items_list)  # [('name', 'John'), ('address', '123 Main St')] 

#Copy a Dictionary
#We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
person_copy = person.copy()
print(person_copy)  # {'name': 'John', 'address': '123 Main St'}    

#Getting Dictionary Keys as a List
#The keys() method gives us all the keys of a a dictionary as a list.
keys_list = list(person.keys())
print(keys_list)  # ['name', 'address'] 

#Getting Dictionary Values as a List
#The values() method gives us all the values of a dictionary as a list.
values_list = list(person.values())
print(values_list)  # ['John', '123 Main St']

#Dictionary Methods
#clear(): removes all items from the dictionary.
#copy(): returns a shallow copy of the dictionary.
#fromkeys(): creates a new dictionary from given keys and a value.
#get(): returns the value of the specified key.
#items(): returns a view object that displays a list of a dictionary's key-value tuple pairs.
#keys(): returns a view object that displays a list of all the keys in the dictionary.
#pop(): removes the item with the specified key name.
#popitem(): removes the last inserted key-value pair.
#setdefault(): returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
#update(): updates the dictionary with the specified key-value pairs.
#values(): returns a view object that displays a list of all the values in the dictionary.      

#Nested Dictionaries
#A nested dictionary is a dictionary inside a dictionary.
student = {
    'name': 'Alice',
    'age': 22,
    'courses': {
        'math': 'A',
        'science': 'B',
        'history': 'A'
    }
}

print(student)
#Accessing Nested Dictionary Items
print(student['courses']['math'])  # 'A'
#Modifying Nested Dictionary Items
student['courses']['science'] = 'A'
print(student['courses'])  # {'math': 'A', 'science': 'A', 'history': 'A'}      



#deleting a dictionary
#del person

#clearing a dictionary
person.clear()
print(person)  # {} 
