# Sets
# Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

# Creating an Empty Set
empty_set = set()
print(empty_set)  # set()
# Creating a Set with Initial Values
fruits = {'apple', 'banana', 'orange'}
print(fruits)  # {'apple', 'banana', 'orange'}
# Creating a Set from a List
numbers_list = [1, 2, 3, 4, 5, 1, 2]
numbers_set = set(numbers_list)
print(numbers_set)  # {1, 2, 3, 4, 5}
# Creating a Set from a String
string_set = set('hello')
print(string_set)  # {'h', 'e', 'l', 'o'}   

# Accessing Set Items
for fruit in fruits:
    print(fruit)   
#set's Length
print(len(fruits))  # 3

#Checking an Item
print('banana' in fruits)  # True
print('grape' in fruits)   # False  

# Adding Items to a Set
fruits.add('grape')
print(fruits)  # {'apple', 'banana', 'orange', 'grape'}
# Adding Multiple Items to a Set
fruits.update(['kiwi', 'mango'])
print(fruits)  # {'apple', 'banana', 'orange', 'grape', 'kiwi', 'mango'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)  # {'banana', 'orange', 'mango', 'lemon', 'tomato', 'potato', 'cabbage', 'onion', 'carrot'}

# Removing Items from a Set
fruits.remove('banana')
print(fruits)  # {'apple', 'orange', 'grape', 'kiwi', 'mango'}
# Discarding an Item (no error if item not found)
fruits.discard('pineapple')  # No error
print(fruits)  # {'apple', 'orange', 'grape', 'kiwi', 'mango'}
# Popping an Item (removes and returns an arbitrary item)
popped_item = fruits.pop()
print("Popped item:", popped_item)
print(fruits)  # Remaining items in the set     

# Clearing a Set
fruits.clear()
print(fruits)  # set()

# Deleting a Set
#del fruits

#Converting List to Set
#We can convert list to set and set to list. 
#Converting list to set removes duplicates and only unique items will be reserved.
numbers_list = [1, 2, 2, 3, 4, 4, 5]
numbers_set = set(numbers_list)
print(numbers_set)  # {1, 2, 3, 4, 5}
#Converting Set to List 
unique_numbers_list = list(numbers_set)
print(unique_numbers_list)  # [1, 2, 3, 4, 5]   


# Set Operations    
# Union
# Joining Sets
#We can join two sets using the union() or update() method.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
# Or using update() method
# set_a.update(set_b)

print("Union:", union_set)  # {1, 2, 3, 4, 5}

# Intersection
set_a = {1, 2, 3}
set_b = {3, 4, 5}
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)  # {3}     

# Difference
set_a = {1, 2, 3}
set_b = {3, 4, 5}
difference_set = set_a.difference(set_b)
print("Difference (A - B):", difference_set)  # {1, 2}
# Symmetric Difference
set_a = {1, 2, 3}
set_b = {3, 4, 5}
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", symmetric_difference_set)  # {1, 2, 4, 5}    
# Subset
set_a = {1, 2}
set_b = {1, 2, 3, 4, 5}
is_subset = set_a.issubset(set_b)
print("Is A a subset of B?", is_subset)  # True
# Superset
set_a = {1, 2, 3, 4, 5}
set_b = {1, 2}
is_superset = set_a.issuperset(set_b)
print("Is A a superset of B?", is_superset)  # True
# Disjoint Set  
set_a = {1, 2}
set_b = {3, 4, 5}
is_disjoint = set_a.isdisjoint(set_b)
print("Are A and B disjoint sets?", is_disjoint)  # True        
# Copying a Set
original_set = {1, 2, 3}
copied_set = original_set.copy()
print("Copied Set:", copied_set)  # {1, 2, 3}   
# Frozen Set
# A frozen set is an immutable version of a set. Once created, we cannot add or remove items from it.
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen Set:", frozen_set)  # frozenset({1, 2, 3, 4, 5})
# Attempting to add or remove items will raise an error
# frozen_set.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
# frozen_set.remove(3)  # AttributeError: 'frozenset' object has
# no attribute 'remove' 
