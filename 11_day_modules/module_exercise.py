# Exercises: Level 1
# Writ a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'
def random_user_id():
    import random
    import string

    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print(random_user_id()) 
# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr

def user_id_gen_by_user():
    import random
    import string

    num_chars = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of IDs to generate: "))

    characters = string.ascii_letters + string.digits
    ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_chars))
        ids.append(user_id)
    
    return ids
print(user_id_gen_by_user())    

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    import random

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f'rgb({r},{g},{b})'
print(rgb_color_gen())  
# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n):
    import random
    colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colors.append(color)
    
    return colors
print(list_of_hexa_colors(3))
# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    import random
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgb({r},{g},{b})')
    
    return colors
print(list_of_rgb_colors(4))
# Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
def generate_colors(color_type, n):
    import random

    colors = []
    if color_type == 'hexa':
        for _ in range(n):
            color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
            colors.append(color)
    elif color_type == 'rgb':
        for _ in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f'rgb({r},{g},{b})')
    
    return colors
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 2))
# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(lst):
    import random
    random.shuffle(lst)
    return lst  
print(shuffle_list([1, 2, 3, 4, 5]))
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    import random
    numbers = random.sample(range(10), 7)
    return numbers
print(unique_random_numbers())  