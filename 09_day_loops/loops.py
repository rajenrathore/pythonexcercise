# Loops
# Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

# while loop
# for loop
#While Loop
# We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.

  # syntaxs
# while condition:
#     code goes here

# Example:

count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

#In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.

#   # syntax
# while condition:
#     code goes here
# else:
#     code goes here
# Example:

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
#The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed

#Break and Continue - Part 1
# In Python, we can use the break and continue statements to alter the flow of a loop.  
# The break statement is used to exit a loop prematurely when a certain condition is met.
count = 0
while count < 10:
    #print(count)
    if count == 5:
        break
    print(count)
    count += 1
# In the above example, the loop will terminate when count reaches 5, and the numbers 0 to 4 will be printed.

# The continue statement is used to skip the current iteration of a loop and move to the next iteration.
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
# In this example, the loop will skip even numbers and only print odd numbers from 1 to 9.  

#For Loop
#A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# syntax
# for item in sequence:
#     code goes here    
# Example:
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in fruits:
    print(fruit)
# In the above example, we are iterating through each fruit in the fruits list and printing it.

# Example with string
for char in "Python":
    print(char)
# In this example, we are iterating through each character in the string "Python" and printing it.  

# Example with range()
for i in range(5):
    print(i)
# In this example, we are using the range() function to generate a sequence of numbers from 0 to 4 and printing each number.

#example with dictionary
person = {'first_name': 'Asabeneh',
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
for key in person:
    print(key, ':', person[key])
# In this example, we are iterating through each key in the person dictionary and printing the
# key along with its corresponding value.   
for key, value in person.items():
    print(key, ':', value)
# In this example, we are using the items() method to get both keys and values from the person dictionary and printing them.    

# example with tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)
# In this example, we are iterating through each number in the numbers tuple and printing it.

# example with set

fruits = {'banana', 'orange', 'mango', 'lemon'}
for fruit in fruits:
    print(fruit)
# In this example, we are iterating through each fruit in the fruits set and printing it.



#Break and Continue - Part 2
# Similar to while loop, we can use break and continue statements in for loop to alter the flow of the loop.
# Example of break statement in for loop
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in fruits:
    if fruit == 'mango':
        break
    print(fruit)
# In the above example, the loop will terminate when it encounters 'mango', and only 'banana' and 'orange' will be printed.     
# Example of continue statement in for loop
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in fruits:
    if fruit == 'mango':
        continue
    print(fruit)
# In this example, the loop will skip 'mango' and print the other fruits:
# 'banana', 'orange', and 'lemon'.  

#The Range Function
#The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range
# Example:  
for i in range(5):
    print(i)
# In this example, the range() function generates numbers from 0 to 4.
for i in range(2, 6):
    print(i)
# In this example, the range() function generates numbers from 2 to 5.  
for i in range(1, 10, 2):
    print(i)
# In this example, the range() function generates numbers from 1 to 9 with a step of 2. 

#Nested Loops
# A nested loop is a loop inside another loop. The "inner loop" will be executed one time for each iteration of the "outer loop".
# Example:
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# In this example, the outer loop iterates through numbers 0 to 2, and for each iteration of the outer loop, the inner loop iterates through numbers 0 to 1


person = {
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
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# for else
for i in range(5):
    print(i)
else:
    print("Loop is over")
# In this example, the else block will be executed after the for loop completes its iterations.

#Pass
#In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
for i in range(5):
    pass

#This concludes our introduction to loops in Python. You can use these constructs to perform repetitive tasks efficiently in your programs.