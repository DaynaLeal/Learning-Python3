letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:


def unique_english_letters(word):
    count = 0
    for letter in letters:
        if (letter in word):
            count += 1
    return count


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# -----------------------------------------------------------------------------

# Write a function named count_char_x that takes a string named word and a single character named x as parameters.
# The function should return the number of times x appears in word.
# Write your count_char_x function here:


def count_char_x(word, x):
    count = 0
    for letter in word:
        if x == letter:
            count += 1
    return count


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# -----------------------------------------------------------------------------

# Write a function named count_multi_char_x that takes a string named word and a string named x.
# This function should do the same thing as the count_char_x function you just wrote -
# it should return the number of times x appears in word. However,
# this time, make sure your function works when x is multiple characters long.
# For example, count_multi_char_x("Mississippi", "iss") should return 2
# Write your count_multi_char_x function here:


def count_multi_char_x(word, x):
    if len(x) == 1:
        count = 0
        for letter in word:
            if x == letter:
                count += 1
    else:
        count = len(word.split(x)) - 1
    return count


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# ----------------------------------------------------------------------------

# Write a function named substring_between_letters that takes a string named word,
# a single character named start, and another character named end.
# This function should return the substring between the first occurrence of start and end in word.
# If start or end are not in word, the function should return word.

# For example, substring_between_letters("apple", "p", "e") should return "pl".
# Write your substring_between_letters function here:


def substring_between_letters(word, start, end):
    s = word.find(start)
    e = word.find(end)
    if e == -1 or s == -1:
        return word
    else:
        return word[s+1:e]


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# -----------------------------------------------------------------------------

# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters.
# This function should return True if every word in sentence has a length greater than or equal to x.

# Write your x_length_words function here:


def x_length_words(sentence, x):
    sentence = sentence.split(" ")
    word_count = len(sentence)
    count = 0
    for word in sentence:
        if len(word) >= x:
            count += 1
    return count == word_count


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

# -----------------------------------------------------------------------------

# Write your check_for_name function here:


def check_for_name(sentence, name):
    return name.upper() in sentence.upper()


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# -----------------------------------------------------------------------------

# Create a function named every_other_letter that takes a string named word as a parameter.
# The function should return a string containing every other letter in word.

# Write your every_other_letter function here:


def every_other_letter(word):
    evens = ''
    for i in range(0, len(word)-1):
        if i == 0 or i % 2 == 0:
            evens += word[i]
    return evens


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

# -----------------------------------------------------------------------------

# Write a function named reverse_string that has a string named word as a parameter.
# The function should return word in reverse.
# Write your reverse_string function here:


def reverse_string(word):
    reverse = ''
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    return reverse


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# -----------------------------------------------------------------------------

# A Spoonerism is an error in speech when the first syllables of two words are switched.
# For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”.
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2.
# Finding the first syllable of a word is a difficult task, so for our function,
# we’re going to switch the first letters of each word.
# Return the two new words as a single string separated by a space.
# Write your make_spoonerism function here:


def make_spoonerism(word1, word2):
    spoon1 = word2[0] + word1[1:]
    spoon2 = word1[0] + word2[1:]
    return spoon1 + " " + spoon2


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# -----------------------------------------------------------------------------

# Create a function named add_exclamation that has one parameter named word.
# This function should add exclamation points to the end of word until word is 20 characters long.
# If word is already at least 20 characters long, just return word.
# Write your add_exclamation function here:


def add_exclamation(word):
    if len(word) >= 20:
        return word
    else:
        count = 20 - len(word)
        for i in range(0, count):
            word += '!'
        return word


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
