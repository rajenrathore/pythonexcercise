# There are four collection data types in Python :

# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
# A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

#Creating a List
#We can create a list by placing different comma-separated values between square brackets [].
#Example:
#Creating an empty list
empty_list = []
print(empty_list) # []  

#Lists with initial values. We use len() to find the length of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

#List can have items of different data types
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
print(lst)

#Accessing List Items Using Positive Indexing
#We access each item in a list using their index. A list index starts from 0. 
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
second_fruit = fruits[1]
third_fruit = fruits[2]
fourth_fruit = fruits[3]
print('First fruit:', first_fruit)   # banana
print('Second fruit:', second_fruit) # orange
print('Third fruit:', third_fruit)   # mango
print('Fourth fruit:', fourth_fruit) # lemon    
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print('Last fruit:', last_fruit)     # lemon

#Accessing List Items Using Negative Indexing
#We can also access list items using negative indexing. The last item has index -1, the second last item has index -2 and so on.
fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
third_last = fruits[-3]
fourth_last = fruits[-4]
print('Last fruit:', last_fruit)       # lemon
print('Second last fruit:', second_last) # mango
print('Third last fruit:', third_last)   # orange
print('Fourth last fruit:', fourth_last) # banana   

#Modifying List Items
#We can modify list items by accessing the index and assigning a new value.
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Original list:', fruits)
fruits[0] = 'avocado'  # changing banana to avocado
print('Modified list:', fruits)
fruits[1] = 'kiwi'     # changing orange to kiwi   
print('Modified list:', fruits)
#Modifying more than one item
fruits[0:2] = ['apple', 'cherry'] # changing avocado and kiwi to apple and cherry
print('Modified list:', fruits) 
#Modifying the last item
fruits[-1] = 'pineapple' # changing lemon to pineapple
print('Modified list:', fruits)
#Modifying more than one item using negative indexing
fruits[-2:] = ['watermelon', 'papaya'] # changing mango and pineapple to watermelon and papaya
print('Modified list:', fruits) 
#Modifying all the items in the list
fruits[:] = ['banana', 'orange', 'mango', 'lemon'] # changing all the items
print('Modified list:', fruits)

#Slicing Items from a List
#Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'pineapple']    
all_fruits = fruits[:]               # getting all items
print('All fruits:', all_fruits)     # ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'pineapple']
some_fruits = fruits[1:4]          # getting items from index 1 to 3
print('Some fruits:', some_fruits)   # ['orange', 'mango', 'lemon']
fruits_from_index_2 = fruits[2:]    # getting items from index 2 to the end
print('Fruits from index 2:', fruits_from_index_2) # ['mango', 'lemon', 'kiwi', 'pineapple']
fruits_up_to_index_3 = fruits[:3]  # getting items from the beginning to index 2    
print('Fruits up to index 3:', fruits_up_to_index_3) # ['banana', 'orange', 'mango']
every_second_fruit = fruits[::2]    # getting every second item
print('Every second fruit:', every_second_fruit) # ['banana', 'mango', 'kiwi']
#Negative Indexing: We can also slice items using negative indexing.
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'pineapple']    
last_three_fruits = fruits[-3:]      # getting last three items
print('Last three fruits:', last_three_fruits) # ['lemon', 'kiwi', 'pineapple']
fruits_up_to_last_3 = fruits[:-3]   # getting all items except the last three
print('Fruits up to last 3:', fruits_up_to_last_3) # ['banana', 'orange', 'mango']
some_fruits_negative = fruits[-4:-1]  # getting items from index -4 to -2
print('Some fruits (negative indexing):', some_fruits_negative) # ['mango', 'lemon', 'kiwi']

#Checking Items in a List
#Checking an item if it is a member of a list using in operator. See the example below.
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Is mango in fruits list?', 'mango' in fruits)   # True
print('Is apple in fruits lisst?', 'apple' in fruits)   # False

#Adding Items to a List
#We can add items to a list using append(), insert() and extend() methods.
fruits = ['banana', 'orange', 'mango', 'lemon']
#Using append() to add an item to the end of the list
fruits.append('kiwi')
print('Fruits after append:', fruits) # ['banana', 'orange', 'mango', 'lemon', 'kiwi']


#Inserting Items into a List
#We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # inserting apple at index 2
print('Fruits after insert:', fruits) # ['banana', 'orange', 'apple', 'mango', 'lemon'] 
#Inserting an item at the beginning of the list
fruits.insert(0, 'avocado') # inserting avocado at index 0
print('Fruits after insert at beginning:', fruits) # ['avocado', 'banana', 'orange', 'apple', 'mango', 'lemon'] 
#Inserting an item at the end of the list
fruits.insert(len(fruits), 'kiwi') # inserting kiwi at the end of the list
print('Fruits after insert at the end:', fruits) # ['avocado', 'banana', 'orange', 'apple', 'mango', 'lemon', 'kiwi']

#Extending a Lists
#We can use extend() method to add multiple items to the end of a list. The extend() method takes an iterable as an argument.
fruits = ['banana', 'orange', 'mango', 'lemon']
tropical_fruits = ['papaya', 'pineapple', 'coconut']
fruits.extend(tropical_fruits)  # adding tropical_fruits list to fruits list
print('Fruits after extend:', fruits) # ['banana', 'orange', 'mango', 'lemon', 'papaya', 'pineapple', 'coconut']
#We can also use extend() method with a tuple or a set.
fruits = ['banana', 'orange', 'mango', 'lemon']
more_fruits = ('grape', 'watermelon') # tuple of fruits
fruits.extend(more_fruits)  # adding more_fruits tuple to fruits list
print('Fruits after extending with tuple:', fruits) # ['banana', 'orange', 'mango', 'lemon', 'grape', 'watermelon']
even_more_fruits = {'kiwi', 'dragonfruit'} # set of fruits
fruits.extend(even_more_fruits)  # adding even_more_fruits set to fruits list
print('Fruits after extending with set:', fruits) # ['banana', 'orange', 'mango', 'lemon', 'grape', 'watermelon', 'kiwi', 'dragonfruit']    

#Removing Items from a List
#We can remove items from a list using remove(), pop(), clear() and del methods.
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi']
#Using remove() to remove an item by its value
fruits.remove('mango')  # removing mango from the list
print('Fruits after remove:', fruits) # ['banana', 'orange', 'lemon', 'kiwi']
#Using pop() to remove an item by its index
removed_fruit = fruits.pop(1)  # removing item at index 1 (orange)
print('Removed fruit:', removed_fruit) # orange
print('Fruits after pop:', fruits) # ['banana', 'lemon', 'kiwi']
#Using pop() to remove the last item
last_fruit = fruits.pop()  # removing the last item (kiwi)
print('Last fruit removed:', last_fruit) # kiwi
print('Fruits after popping last item:', fruits) # ['banana', 'lemon']
#Using clear() to remove all items from the list
fruits.clear()
print('Fruits after clear:', fruits) # []
#Using del to delete the entire list
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi']
fruits = ['banana', 'orange', 'mango', 'lemon']
#del fruits
# deleting the fruits single item in list
del fruits[1] # only a single item
print('Fruits after deleting index 1:', fruits) # ['banana', 'mango', 'lemon']
# deleting the entire list
#del fruits  
# print(fruits) # This will raise an error because the list is deleted

# clearing the list using clear() method
fruits.clear()
print('Fruits after clearing the list:', fruits) # []


#Copying a List
#It is possible to copy a list by reassigning it to a new variable in the following way: 
#list2 = list1. Now, list2 is a reference of list1, 
#any changes we make in list2 will also modify the original, list1. 
#But there are lots of case in which we do not like to modify the original 
#instead we like to have a different copy. 
#One of way of avoiding the problem above is using copy().

original_list = ['banana', 'orange', 'mango', 'lemon']
copied_list = original_list.copy()  # copying the original list
print('Original list:', original_list) # ['banana', 'orange', 'mango', 'lemon']
print('Copied list:', copied_list)     # ['banana', 'orange', 'mango', 'lemon']
#Modifying the copied list
copied_list.append('kiwi')
print('Modified copied list:', copied_list) # ['banana', 'orange', 'mango', 'lemon', 'kiwi']
print('Original list after modifying copied list:', original_list) # ['banana', 'orange', 'mango', 'lemon']

#Joining Lists
#There are several ways to join, or concatenate, two or more lists in Python.

#Plus Operator (+)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
joined_list = list1 + list2
print('Joined list using + operator:', joined_list) # ['a', 'b', 'c', 1, 2, 3]
#Using extend() method
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2) 
print('Joined list using extend():', list1) # ['a', 'b', 'c', 1, 2, 3]
#Using unpacking operator (*)
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
joined_list = [*list1, *list2]
print('Joined list using unpacking operator:', joined_list) # ['a', 'b', 'c', 1, 2, 3]

#counting List Items
#The count() method returns the number of times an item appears in a list:
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana', 'kiwi', 'banana']
banana_count = fruits.count('banana')
print('Number of bananas in the list:', banana_count) # 3

#Finding Index of an Item
#The index() method returns the index of an item in the list:
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi']
mango_index = fruits.index('mango')
print('Index of mango in the list:', mango_index) # 2

#Reversing a List
#The reverse() method reverses the order of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print('Reversed list:', fruits) # ['lemon', 'mango', 'orange', 'banana']

#Sorting Listsaaccac
#To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()  # sorting in ascending order
print('Sorted list (ascending):', fruits) # ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)  # sorting in descending order
print('Sorted list (descending):', fruits) # ['orange', 'mango', 'lemon', 'banana']
#Using sorted() function
fruits = ['banana', 'orange', 'mango', 'lemon']
sorted_fruits = sorted(fruits)  # sorting in ascending order
print('Sorted list using sorted() (ascending):', sorted_fruits) # ['banana', 'lemon', 'mango', 'orange']
sorted_fruits_desc = sorted(fruits, reverse=True)  # sorting in descending order
print('Sorted list using sorted() (descending):', sorted_fruits_desc) # ['orange', 'mango', 'lemon', 'banana']


