# dictionaries seem kinda like js objects
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

# --------------------------------------------------------------------------------------------
translations = {'mountain': 'orod', 'bread': 'bass', 'friend': 'mellon', 'horse': 'roch'}

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

my_empty_dictionary = {}

# --------------------------------------------------------------------------------------------

# HOW TO ADD TO A DICTIONARY
animals_in_zoo = {}

animals_in_zoo["zebras"] = 8

animals_in_zoo["monkeys"] = 12

animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

# --------------------------------------------------------------------------------------------

# HOW TO ADD MULTIPLE AT ONCE
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)

# --------------------------------------------------------------------------------------------

# ADDING A KEY VALUE PAIR IN WHICH THE KEY ALREADY EXISTS JUST UPDATES THE VALUE
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners['Supporting Actress'] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)

# --------------------------------------------------------------------------------------------

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}

print(drinks_to_caffeine)

# --------------------------------------------------------------------------------------------

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)

plays['Purple Haze'] = 1
plays['Respect'] = 94
print(plays)

library = {'The Best Songs': plays, 'Sunday Feelings': {}}
print(library)
