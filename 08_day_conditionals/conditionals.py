# Conditionals
# By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

# Conditional execution: a block of one or more statements will be executed if a certain expression is true
# Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.
# If Condition
# In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.
x = 10
if x > 5:
    print("x is greater than 5")    
# If-Else Condition 
# The if statement can be followed by an optional else statement. The else statement will be executed if the condition is false.
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
# If-Elif-Else Condition
# The if statement can be followed by one or more elif statements. The elif statement allows you    
# to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is less than or equal to 5")
# Nested If Condition   
# You can use one if or else if statement inside another if or else if statement(s). This is called nested if statement.
x = 15
if x > 10:
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is greater than 10 but less than or equal to 20")
else:
    print("x is less than or equal to 10")
# You can also use logical operators (and, or, not) to combine multiple conditions in a single if statement.
x = 8
if x > 5 and x < 10:
    print("x is between 5 and 10")  
if x < 5 or x > 10:
    print("x is either less than 5 or greater than 10")  
if not x > 10:
    print("x is not greater than 10")
# This concludes our introduction to conditionals in Python. You can use these constructs to control the flow of your programs based on different conditions.