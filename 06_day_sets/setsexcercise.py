# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'Instagram'])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)     
# What is the difference between remove and discard
# The remove() method raises a KeyError if the specified item is not found in the set, while discard() does not raise an error if the item is not found.

# Exercises: Level 2
# Join A and B
union_set = A.union(B)
print("A union B:", union_set)  
# Find A intersection B
intersection_set = A.intersection(B)
print("A intersection B:", intersection_set)

# Is A subset of B
is_subset = A.issubset(B)
print("Is A subset of B?", is_subset)
# Are A and B disjoint sets
is_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", is_disjoint)    

# Join A with B and B with A
joined_A_B = A.union(B)
joined_B_A = B.union(A)
print("Joined A with B:", joined_A_B)
print("Joined B with A:", joined_B_A)   
# What is the symmetric difference between A and B
symmetric_difference_set = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference_set)
# Delete the sets A and B
#del A
#del B
# Delete the sets completely
#del it_companies


# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
print("Length of age list:", len(age))
print("Length of ages set:", len(ages_set))

# The list is bigger because it contains duplicate values while the set only contains unique values.

# Explain the difference between the following data types: string, list, tuple and set
# A string is a sequence of characters used to represent text. It is immutable, meaning it cannot be changed after creation.
# A list is an ordered collection of items that can be changed (mutable). It allows duplicate values and is defined using square brackets [].
# A tuple is an ordered collection of items that cannot be changed (immutable). It allows duplicate values and is defined using parentheses ().
# A set is an unordered collection of unique items. It does not allow duplicate values and is defined using curly braces {}.    

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split()
unique_words = set(words)
print("Unique words in the sentence:", unique_words)
print("Number of unique words:", len(unique_words)) 
