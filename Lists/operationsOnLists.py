# finding length using len()
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

# --------------------------------------------------------
# how to access by index (zero indexed also)
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(index4)
print(len(employees))
print(employees[1])

# --------------------------------------------------------
# use [-1] to get last element in a list
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))

last_element = shopping_list[-1]
element5 = shopping_list[5]

print(last_element)
print(element5)

# --------------------------------------------------------
# slicing lists using list_name[start:end+1]
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
print(beginning)  # ['shirt', 'shirt', 'pants', 'pants']

middle = suitcase[2:4]
print(middle)  # ['pants', 'pants']

# the zero is redundant when getting the first few from a list
start = suitcase[:3]
print(start)  # ['shirt', 'shirt', 'pants']

# you can use negatives to get the last few from a list too
end = suitcase[-2:]
print(end)  # ['pajamas', 'books']

# --------------------------------------------------------
# counting elements in a list using .count()
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)

# --------------------------------------------------------
# sorting lists using .sort()
# note that .sort() changes the list but doesnt return anything so cannot be saved to a new variable
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()
print(addresses)

names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)

cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
print(sorted_cities)  # prints None since nothing is returned using .sort()

# apparently, you can also use sorted(), which actually does return a new list but doesnt change the old one
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
print(games_sorted)  # ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']
print(games)  # ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

# --------------------------------------------------------
# REVIEW
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
print(inventory_len)

first = inventory[0]
print(first)

last = inventory[-1]
print(last)

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

first_3 = inventory[:3]
print(first_3)

twin_beds = inventory.count('twin bed')
print(twin_beds)

inventory.sort()
print(inventory)

