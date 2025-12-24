# Tuples
# A tuple is a collection of different data types which is ordered and unchangeable(immutable). 
#Tuples are written with round brackets, (). 
#Once a tuple is created, we cannot change its values. 
#We cannot use add, insert, remove methods in a tuple 
#because it is not modifiable (mutable). Unlike list, tuple has few methods. 
#Methods related to tuples:

# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple
# Creating a Tuple

# empty tuple
empty_tuple = ()
print(empty_tuple)  # ()
# tuple with integers
int_tuple = (1, 2, 3, 4, 5)
print(int_tuple)  # (1, 2, 3, 4, 5)
# tuple with mixed data types
mixed_tuple = (1, "Hello", 3.4, True)
print(mixed_tuple)  # (1, 'Hello', 3.4, True)
# tuple with nested tuples
nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple)  # (1, 2, (3, 4), (5, 6))
# Creating a tuple using tuple() method
tuple_from_list = tuple([1, 2, 3, 4, 5])
print(tuple_from_list)  # (1, 2, 3, 4, 5)

#Tuple length
#We use the len() method to get the length of a tuple.
sample_tuple = (1, 2, 3, 4, 5)
print(len(sample_tuple))  # 5   

# Accessing Tuple Items
#We can access tuple items by referring to the index number, inside square brackets [].
sample_tuple = ('a', 'b', 'c', 'd', 'e')
print(sample_tuple[0])  # 'a'
print(sample_tuple[2])  # 'c'
print(sample_tuple[-1])  # 'e'
print(sample_tuple[-3])  # 'c'  
#Slicing Tuples
#We can slice a tuple just like we slice a list or string.
sample_tuple = (0, 1, 2, 3, 4, 5)
print(sample_tuple[1:4])  # (1, 2, 3)
print(sample_tuple[:3])   # (0, 1, 2)
print(sample_tuple[3:])   # (3, 4, 5)
print(sample_tuple[-4:-1])  # (2, 3, 4) 

#Unpacking Tuples
#We can unpack tuple items into variables.
sample_tuple = (1, 2, 3)
a, b, c = sample_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3   
#Tuple Methods
# count(): returns the number of times a specified value occurs in a tuple.
sample_tuple = (1, 2, 2, 3, 4, 2)
print(sample_tuple.count(2))  # 3
# index(): searches the tuple for a specified value and returns the position of where it was found.
sample_tuple = ('a', 'b', 'c', 'd', 'e')
print(sample_tuple.index('c'))  # 2 
#Joining Tuples
#We can join two or more tuples to create a new tuple using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2
print(joined_tuple)  # (1, 2, 3, 4, 5, 6)
#Multiplying Tuples
#We can multiply tuples using the * operator to create a new tuple with repeated elements.
sample_tuple = ('a', 'b', 'c')
multiplied_tuple = sample_tuple * 3
print(multiplied_tuple)  # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')
#Tuple Membership
#We can check if an item exists in a tuple using the 'in' keyword.
sample_tuple = (1, 2, 3, 4, 5)
print(3 in sample_tuple)  # True
print(6 in sample_tuple)  # False       


#Changing Tuples to Lists
#We can change tuples to lists and lists to tuples. 
#Tuple is immutable if we want to modify a tuple we should change it to a list.
sample_tuple = (1, 2, 3)
temp_list = list(sample_tuple)  # Convert tuple to list
temp_list.append(4)             # Modify the list
modified_tuple = tuple(temp_list)  # Convert back to tuple
print(modified_tuple)  # (1, 2, 3, 4)   

#Deleting a Tuple
#We can delete a tuple using the del keyword.
sample_tuple = (1, 2, 3)
del sample_tuple
# print(sample_tuple)  # This will raise an error because the tuple has been deleted
#Note: Since tuples are immutable, we cannot change, add, or remove items after the tuple is created.
#However, we can delete the entire tuple using the del keyword as shown above.