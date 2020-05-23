# you can iterate through lists using a for loop with syntax:
# for <temporary variable> in <list variable>:
#     <action>
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)

# ------------------------------------------------------------------------------------------
# temp variable can be named anything
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
    print(game)

for sport in sport_games:
    print(sport)

# ------------------------------------------------------------------------------------------
# using range in loops (to iterate and count)
promise = "I will not chew gum in class"
for i in range(5):
    print(promise)

# ------------------------------------------------------------------------------------------
# be sure not to create an infinite loop, or use control+C (or refresh if an online editor)
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)
    print(student)

# ------------------------------------------------------------------------------------------
# use break to stop in a loop early
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
    print(dog)
    if dog == dog_breed_I_want:
        print("They have the dog I want!")
        break


# ------------------------------------------------------------------------------------------
# continue to skip
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
    if age < 21:
        continue
    print(age)

# ------------------------------------------------------------------------------------------
# while loops
index = 0
while index < len(dog_breeds):
    print(dog_breeds[index])
    index += 1

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

i = 0
while i < 6:
    student = all_students.pop()
    students_in_poetry.append(student)
    i += 1

print(students_in_poetry)

# ------------------------------------------------------------------------------------------
# nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for list in sales_data:
    for num in list:
        scoops_sold += num

print(scoops_sold)

# ------------------------------------------------------------------------------------------
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
    if word[0] == '@':  # note here that you can access a character of a string using index
        usernames.append(word)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = []

for height in heights:
    if height > 161:
        can_ride_coaster.append(height)

print(can_ride_coaster)

# ------------------------------------------------------------------------------------------
# updating lists by iterating with for loop
celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp * (9/5) + 32 for temp in celsius]

print(fahrenheit)

# ------------------------------------------------------------------------------------------
# REVIEW
# ------------------------------------------------------------------------------------------
single_digits = list(range(10))
print(single_digits)

squares = []

for digit in single_digits:
    square = digit**2
    squares.append(square)

print(squares)

cubes = [digit**3 for digit in single_digits]
print(cubes)
