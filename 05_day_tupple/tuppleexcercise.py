# Create an empty tuple

empty_tuple = ()
print(empty_tuple)  # ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('John', 'Mike')
sisters = ('Anna', 'Kate')
print(brothers)
print(sisters) 
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('tover', 'jena')
print(family_members)


# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings = family_members[:len(brothers) + len(sisters)]
parents = family_members[len(brothers) + len(sisters):]
print("Siblings:", siblings)
print("Parents:", parents)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index:middle_index + 1]
print("Middle item(s):", middle_items)  
# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)
# Delete the food_staff_tp tuple completely
#del food_stuff_tp
# Check if an item exists in tuple:
apple_exists = 'apple' in food_stuff_tp
print("Is apple in food_stuff_tp?", apple_exists)
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
estonia_exists = 'Estonia' in nordic_countries
iceland_exists = 'Iceland' in nordic_countries
print("Is Estonia a nordic country?", estonia_exists)
print("Is Iceland a nordic country?", iceland_exists)