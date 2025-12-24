# Declare an empty list
empty_list = []
# Declare a list with more than 5 items
mixed_list = [1, 'hello', 3.14, True, [1, 2, 3], {'key': 'value'}]

# Find the length of your list
print("Length of mixed_list:", len(mixed_list))

# Get the first item, the middle item and the last item of the list
first_item = mixed_list[0]
middle_item = mixed_list[len(mixed_list) // 2]
last_item = mixed_list[-1]
print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["John", 25, 5.8, "Single", "123 Main Street"]
print("Mixed data types list:", mixed_data_types)
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
print("IT Companies:", it_companies)
# Print the number of companies in the list
print("Number of IT Companies:", len(it_companies))
# Print the first, middle and last company
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies) // 2])
print("Last company:", it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = "Meta"
print("IT Companies after modification:", it_companies)

# Add an IT company to it_companies
it_companies.append("Netflix")
print("IT Companies after adding Netflix:", it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Tesla")
print("IT Companies after inserting Tesla:", it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print("IT Companies after changing Google to uppercase:", it_companies)

# Join the it_companies with a string '#;  '
joined_companies = ' #; '.join(it_companies)
print("Joined IT Companies:", joined_companies)
# Check if a certain company exists in the it_companies list.
print("Does Netflix exist in it_companies?", "Netflix" in it_companies)
# Sort the list using sort() method
it_companies.sort()
print("IT Companies after sorting:", it_companies)
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print("IT Companies after reversing:", it_companies)
# Slice out the first 3 companies from the list
first_three = it_companies[:3]
print("First three companies:", first_three)
# Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print("Last three companies:", last_three)
# Slice out the middle IT company or companies from the list
middle_company = it_companies[len(it_companies) // 2]
print("Middle company:", middle_company)
# Remove the first IT company from the list
it_companies.pop(0)
print("IT Companies after removing first company:", it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)
print("IT Companies after removing middle company:", it_companies)

# Remove the last IT company from the list
it_companies.pop()
print("IT Companies after removing last company:", it_companies)

# Remove all IT companies from the list
#it_companies.clear()
print("IT Companies after clearing:", it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print("Full Stack List:", full_stack)