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

# --------------------------------------------------------------------------------------------
# SECOND LESSON ON DICTIONARIES
# --------------------------------------------------------------------------------------------

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# --------------------------------------------------------------------------------------------

# check to see if key is in the dictionary before printing
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

key_to_check = "energy"

if key_to_check in zodiac_elements:
    print(zodiac_elements["energy"])

# --------------------------------------------------------------------------------------------

# you can also use a try/except block to check
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, "matcha": 30}

key_check = "matcha"
try:
    print(caffeine_level[key_check])
except:
    print("Unknown Caffeine Level")

# --------------------------------------------------------------------------------------------

# you can find using .get() without worrying about a try/except block
# you can provide a default value with second parameter
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# --------------------------------------------------------------------------------------------

# use .pop() to find, set a default and delete a key value pair
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)

health_points += available_items.pop("power stew", 0)

health_points += available_items.pop("mystic bread", 0)

print(health_points)

# --------------------------------------------------------------------------------------------

# to return an object of keys
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

list(user_ids)
list(num_exercises)

# --------------------------------------------------------------------------------------------

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for value in num_exercises.values():
    total_exercises += value

print(total_exercises)

# --------------------------------------------------------------------------------------------

# iterate through both using .items() to return a tuple
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for job, pct in pct_women_in_occupation.items():
    print("Women make up " + str(pct) + " percent of " + job + "s.")

# --------------------------------------------------------------------------------------------

# REVIEW
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

print(spread)

for time, card in spread.items():
    print("Your " + time + " is the " + card + " card.")
