#Check the data type of all your variables using type() built-in function
first_name = 'rajendra'
last_name = 'rathore'
age = 34
is_married = True
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(is_married))
#Using the len() built-in function, find the length of your first name
print(len(first_name))
#Compare the length of your first name and your last name
print(len(first_name))
print(len(last_name))
#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print('total:', total)
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print('diff:', diff)
#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print('product:', product)
#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print('division:', division)
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
reminder = num_one % num_two
print('reminder:', reminder)
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = pow(num_one, num_two)
print('exp:', exp)
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print('floor_division:',floor_division)
#The radius of a circle is 30 meters.
r = 30
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14*r*r
print('area_of_circle:',area_of_circle)
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*3.14*r
print('circum_of_circle:',circum_of_circle)
#Take radius as user input and calculate the area.
radius = float(input('enter radius of circle '))
circle_area = 3.14*radius*radius
print(circle_area)
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

country = input("Enter your country: ")

age = int(input("Enter your age: "))

print("\n--- User Information ---")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
