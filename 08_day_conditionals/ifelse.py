#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need to wait {years_left} more years to drive.")    

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 25  # You can change this value to your actual age
your_age = int(input("Enter your age: "))
if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_diff} years older than you.")
elif your_age > my_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
else:
    print("We are the same age.")  
#Get two numbers from user using input(“Enter first number: ”) and input(“Enter second number: ”). If first number is greater than second, print first is greater than second. If first number is less than second, print first is smaller than second, otherwise print they are equal. Output:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}.")
else:
    print("Both numbers are equal.")

#Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

score = float(input("Enter your score (0-100): "))
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score < 80:
    grade = 'B'
elif 60 <= score < 70:
    grade = 'C'
elif 50 <= score < 60:
    grade = 'D'
elif 0 <= score < 50:
    grade = 'F'
else:
    grade = None
    print("Invalid score. Please enter a score between 0 and 100.") 
if grade:
    print(f"Your grade is: {grade}")

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter the month: ").strip().lower()
if month in ['september', 'october', 'november']:
    season = 'Autumn'
elif month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
else:
    season = None
    print("Invalid month name.")
if season:
    print(f"The season is {season}.")
#The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_check = input("Enter a fruit name: ").strip().lower()
if fruit_to_check in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit_to_check)
    print("Modified fruit list:", fruits)  

#Check if a person is eligible to vote. A person is eligible to vote if his/her age is greater than or equal to 18. Output:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")  
#Check if a number is even or odd using if else condition. Output:
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

##########################################################################

#Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])
    
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person['skills']:
    print("The person has Python skill.")
else:
    print("The person does not have Python skill.")

# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    skills = set(person['skills'])
    if skills == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif skills == {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif skills == {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('unknown title')

# * If the person is married and if he lives in Finland, print the information in the following format:
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.") 