# formatted like js array
heights = [61, 70, 67, 64, 65]

# --------------------------------------------------------------------------------------
# they can contain mixed types
ints_and_strings = [1, 2, 3, 'four', 'five', 'six']
sam_height = ['Sam', 67]

# --------------------------------------------------------------------------------------
# lists can also contain lists
heights2 = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
ages = [['Aaron', 15], ['Dhruti', 16]]

# --------------------------------------------------------------------------------------
# zip(x, y) will intake two lists and pair up their values, returns memory address like Java
# so you must use print(list(zip_name)) to print to console
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
print(names_and_dogs_names)  # prints <zip object at 0x7f9fc4af0ac8>

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)  # prints [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'),
# ('Sam', 'Carter'), ('Grace', 'Ralph')]

# --------------------------------------------------------------------------------------
# empty lists can be created
empty_list = []
my_empty_list = []

# --------------------------------------------------------------------------------------
# you can add to empty lists (or the end of any list) by using empty_list_name.append(x)
orders = ['daisies', 'periwinkle']
print(orders)  # ['daisies', 'periwinkle'']

orders.append('tulips')
print(orders)  # ['daisies', 'periwinkle', 'tulips']

orders.append('roses')
print(orders)  # ['daisies', 'periwinkle', 'tulips', 'roses']

# --------------------------------------------------------------------------------------
# you can concatenate lists with a plus + but wont save unless you store to a new variable
orders2 = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:
new_orders = orders2 + ['lilac', 'iris']
print(new_orders)
print(orders2)

broken_prices = [5, 3, 4, 5, 4] + [4]

# --------------------------------------------------------------------------------------
# range(10) will give a list of values 0-9 (one less than input)
# also must be converted back to a list from a memory address
list1 = list(range(9))
list2 = list(range(8))

# using range(x, y) with two numbers will give you a list including x up to y-1
list(range(2, 9))  # will give 2-8

# using range (x, y, z) will give you range x up to y-1 skipping every zth value
list(range(2, 9, 2))  # will give [2,4,6,8]

# --------------------------------------------------------------------------------------
# REVIEW
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

age = []
age.append(42)

all_ages = [32, 41, 29] + age

name_and_age = zip(first_names, all_ages)
ids = range(0, 4)

# --------------------------------------------------------------------------------------





