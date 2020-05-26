favorite_word = "progress"
print(favorite_word)

# ---------------------------------------------------------------------------------

my_name = "Dayna"
first_initial = my_name[0]
print(first_initial)

# ---------------------------------------------------------------------------------

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
print(new_account)

temp_password = last_name[2:6]
print(temp_password)

# ---------------------------------------------------------------------------------

first_name2 = "Julie"
last_name2 = "Blevins"


def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]


new_account = account_generator(first_name2, last_name2)

# ---------------------------------------------------------------------------------

first_name3 = "Reiko"
last_name3 = "Matsuki"


def password_generator(first_name, last_name):
    last_length = len(last_name)
    first_length = len(first_name)
    return first_name[first_length-3:] + last_name[last_length-3:]


temp_password = password_generator(first_name3, last_name3)
print(temp_password)

# ---------------------------------------------------------------------------------

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
print(second_to_last)
final_word = company_motto[-4:]
print(final_word)

# ---------------------------------------------------------------------------------
# Strings are immutable and cannot be changed

first_name5 = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name5[1:]
print(fixed_first_name)

# ---------------------------------------------------------------------------------
# backslash as an escape
password = "theycallme\"crazy\"91"

# ---------------------------------------------------------------------------------

# you can iterate through strings with loops


def get_length(str):
    count = 0
    for letter in str:
        count += 1
    return count


# ---------------------------------------------------------------------------------


def letter_check(word, letter):
    for character in word:
        if character == letter:
            return True
    return False


# ---------------------------------------------------------------------------------

def contains(big_string, little_string):
    return little_string in big_string


def common_letters(string_one, string_two):
    bucket = []
    for letter in string_one:
        if (letter in string_two) and not (letter in bucket):
            bucket.append(letter)
    return bucket


# ---------------------------------------------------------------------------------

def username_generator(first_name, last_name):
    username = first_name[:3] + last_name[:4]
    return username


def password_generator(username):
    password = username[-1] + username[0:(len(username)-1)]
    return password

