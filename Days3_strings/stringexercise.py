#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
con_string = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(con_string)
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
con_string2 = 'Coding' + ' ' + 'For' + ' ' + 'All' 
print(con_string2)
#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
#Cut(slice) out the first word of Coding For All string.
first_word = company.split()[0]
print(first_word)
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))  # returns the starting index of the substring
print(company.index('Coding'))  # returns the starting index of the substring

#Replace the word coding in the string 'Coding For All' to Python.
new_company = company.replace('Coding', 'Python')
print(new_company)
#Change Python for Everyone to Python for All using the replace method or other methods.
python_for_everyone = "Python for Everyone"
python_for_all = python_for_everyone.replace('Everyone', 'All')
print(python_for_all)
#Split the string 'Coding For All' using space as the separator (split()) .
split_company = company.split(' ')
print(split_company)
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_tech_companies = tech_companies.split(', ')
print(split_tech_companies)
#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(len(company) - 1)
#What character is at index 10 in "Coding For All" string.
print(company[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'
acronym = ''.join([word[0] for word in phrase.split()])
print(acronym)
#Create an acronym or an abbreviation for the name 'Coding For All'.
phrase2 = 'Coding For All'
acronym2 = ''.join([word[0] for word in phrase2.split()])
print(acronym2)
#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.index('because'))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start = sentence.index('because')
end = sentence.rindex('because') + len('because')
sliced_phrase = sentence[start:end]
print(sliced_phrase)

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
start_index = sentence.find('because')
end_index = sentence.rfind('because') + len('because')
sliced_phrase = sentence[start_index:end_index]
print(sliced_phrase)
#Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))   
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
messy_string = '   Coding For All      '
cleaned_string = messy_string.strip()
print(cleaned_string)

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print(var1.isidentifier())  # False, because it starts with a digit
print(var2.isidentifier())  # True, valid identifier

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
print('Asabeneh\t250\tFinland\tHelsinki')
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))
# Make the following using an f-string:
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}") 